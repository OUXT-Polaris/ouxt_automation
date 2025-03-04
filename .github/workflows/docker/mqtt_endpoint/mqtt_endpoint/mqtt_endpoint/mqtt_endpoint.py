import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.motor_command import MotorCommand
from mqtt_endpoint.ground_station_heartbeat_pb2 import ground_station_heartbeat


class MqttEndPoint:
    heartbeat_topic = "miniv/heartbeat"
    disconnection_count = 0
    broker_ip = "2.tcp.ngrok.io"
    mqtt_port = 12028
    estop_ip = "192.168.0.103"
    estop_port = 4000
    keep_alive_timeout = 10

    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.left_motor_command = MotorCommand(
            "192.168.0.102",
            8888,
            "miniv/left_motor",
        )
        self.right_motor_command = MotorCommand(
            "192.168.0.50",
            8888,
            "miniv/right_motor",
        )
        self.heartbeat_command = ground_station_heartbeat()
        self.heartbeat_command.sequence = 1
        self.heartbeat_command.mode = 1
        print("Start connecting to MQTT Broker")
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(
            self.broker_ip, self.mqtt_port, self.keep_alive_timeout
        )

    def start_loop(self):
        self.mqtt_client.loop_forever()

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
            # Subscribe all topics
            client.subscribe("#")
        else:
            print(f"Connection failed with code {rc}")

    def on_disconnect(self, client, userdata, rc):
        if rc != 0:
            print(f"Unexpected disconnection. Reconnecting... (rc={rc})")
            time.sleep(5)
            try:
                client.reconnect()
            except Exception as e:
                print(f"Reconnection failed: {e}")

    def on_message(self, client, userdata, msg):
        if msg.topic == self.left_motor_command.command_topic:
            self.left_motor_command.send_command_from_serialized_string(msg.payload)
            self.right_motor_command.send_command()
        if msg.topic == self.right_motor_command.command_topic:
            self.left_motor_command.send_command()
            self.right_motor_command.send_command_from_serialized_string(msg.payload)
        if msg.topic == "ground_station/heartbeat":
            self.udp_socket.sendto(
                msg.payload,
                (self.estop_ip, self.estop_port),
            )
            if self.heartbeat_command.mode == 0:
                print("mode: AUTO")
            elif self.heartbeat_command.mode == 1:
                print("mode: MANUAL")
            elif self.heartbeat_command.mode == 2:
                print("mode: ESTOP")
            self.heartbeat_command.ParseFromString(msg.payload)
            self.left_motor_command.set_mode(self.heartbeat_command.mode)
            self.right_motor_command.set_mode(self.heartbeat_command.mode)
            self.right_motor_command.send_command()
            self.left_motor_command.send_command()


def main():
    endpoint = MqttEndPoint()
    try:
        endpoint.start_loop()
    except KeyboardInterrupt:
        print("Exiting...")
    # finally:
    #     endpoint.stop_all_motors()


if __name__ == "__main__":
    main()
