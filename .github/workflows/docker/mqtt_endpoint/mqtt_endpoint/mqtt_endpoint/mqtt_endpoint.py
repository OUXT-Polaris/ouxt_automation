import time
import socket
import sched
import paho.mqtt.client as mqtt
from mqtt_endpoint.motor_command import MotorCommand
from mqtt_endpoint.ground_station_heartbeat import GroundStationHeartBeat


class MqttEndPoint:
    heartbeat_topic = "miniv/heartbeat"
    disconnection_count = 0
    broker_ip = "54.212.20.15"
    mqtt_port = 1883
    estop_ip = "192.168.0.103"
    keep_alive_timeout = 10

    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.left_motor_command = MotorCommand(
            self.udp_socket,
            "192.168.0.102",
            8888,
            4000,
            "miniv/left_motor",
            self.scheduler,
        )
        self.right_motor_command = MotorCommand(
            self.udp_socket,
            "192.168.0.101",
            8888,
            4000,
            "miniv/right_motor",
            self.scheduler,
        )
        self.groundstation_heartbeat = GroundStationHeartBeat(
            "ground_station/heartbeat", 1.0, self.scheduler
        )
        print("Start connecting to MQTT Broker")
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(
            self.broker_ip, self.mqtt_port, self.keep_alive_timeout
        )

    def send_estop_heartbeat(self, scheduler):
        if not client.is_connected():
            scheduler.enter(0.1, 1, self.send_estop_heartbeat, (scheduler,))
        else:
            self.stop_all_motors()

    def start_loop(self):
        self.mqtt_client.loop_start()
        self.scheduler.run()

    def stop_all_motors(self):
        self.right_motor_command.stop = True
        self.left_motor_command.stop = True
        # Wait for graceful shutting down.
        time.sleep(1)

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
        if msg.topic == self.groundstation_heartbeat.topic:
            self.groundstation_heartbeat.receive()


def main():
    endpoint = MqttEndPoint()
    try:
        endpoint.start_loop()
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        endpoint.stop_all_motors()


if __name__ == "__main__":
    main()
