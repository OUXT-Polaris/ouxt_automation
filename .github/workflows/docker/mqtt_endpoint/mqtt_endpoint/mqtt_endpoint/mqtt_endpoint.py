import time
import socket
import sched
import paho.mqtt.client as mqtt
from mqtt_endpoint.motor_command import MotorCommand
from mqtt_endpoint.ground_station_heartbeat import GroundStationHeartBeat
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
        self.heartbeat_command = ground_station_heartbeat()
        self.heartbeat_command.sequence = 1
        self.heartbeat_command.mode = 1
        self.groundstation_heartbeat = GroundStationHeartBeat(
            "ground_station/heartbeat", 3.0, self.scheduler
        )
        print("Start connecting to MQTT Broker")
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(
            self.broker_ip, self.mqtt_port, self.keep_alive_timeout
        )
        self.send_estop_heartbeat(self.scheduler)

    def send_estop_heartbeat(self, scheduler):
        if self.mqtt_client.is_connected():
            self.heartbeat_command.sequence = self.heartbeat_command.sequence + 1
            self.udp_socket.sendto(
                ground_station_heartbeat.SerializeToString(self.heartbeat_command),
                (self.estop_ip, self.estop_port),
            )
        scheduler.enter(0.1, 1, self.send_estop_heartbeat, (scheduler,))
        # else:
        #     self.stop_all_motors()

    def start_loop(self):
        self.mqtt_client.loop_start()
        self.scheduler.run()

    # def stop_all_motors(self):
    #     self.right_motor_command.stop = True
    #     self.left_motor_command.stop = True
    #     # Wait for graceful shutting down.
    #     time.sleep(1)

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
            # print("Left")
            # print(self.left_motor_command.command.motor_speed)
            # print(self.left_motor_command.command.mode)
        if msg.topic == self.right_motor_command.command_topic:
            self.left_motor_command.send_command()
            self.right_motor_command.send_command_from_serialized_string(msg.payload)
        if msg.topic == self.groundstation_heartbeat.topic:
            if self.heartbeat_command.mode == 0:
                print("mode: AUTO")
            elif self.heartbeat_command.mode == 1:
                print("mode: MANUAL")
            elif self.heartbeat_command.mode == 2:
                print("mode: ESTOP")
            self.groundstation_heartbeat.receive(msg.payload)
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
