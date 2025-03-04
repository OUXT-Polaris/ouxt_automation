import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.motor_command import MotorCommand


class MqttEndPoint:
    heartbeat_topic = "miniv/heartbeat"
    lwt_topic = "client/status"
    lwt_message = "Remote motor control command disconnected"
    disconnection_count = 0
    broker_ip = "54.212.20.15"
    mqtt_port = 1883
    estop_ip = "192.168.0.103"
    keep_alive_timeout = 1

    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.left_motor_command = MotorCommand(
            self.udp_socket, "192.168.0.102", 8888, 4000, "miniv/left_motor"
        )
        self.right_motor_command = MotorCommand(
            self.udp_socket, "192.168.0.101", 8888, 4000, "miniv/right_motor"
        )
        print("Start connecting to MQTT Broker")
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.connect(
            self.broker_ip, self.mqtt_port, self.keep_alive_timeout
        )
        self.mqtt_client.loop_start()
        # Wait until the connection was established.
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
            left_motor_command.send_command_from_serialized_string(msg.payload)
            right_motor_command.send()
        if msg.topic == self.right_motor_command.command_topic:
            left_motor_command.send()
            right_motor_command.send_command_from_serialized_string(msg.payload)


def main():
    MqttEndPoint()


if __name__ == "__main__":
    main()
