import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.motor_command import MotorCommand


class MqttEndPoint:
    heartbeat_topic = "miniv/heartbeat"
    lwt_topic = "client/status"
    lwt_message = "Remote motor control command disconnected"
    left_motor_control_topic = "miniv/left_motor"
    right_motor_control_topic = "miniv/right_motor"
    disconnection_count = 0
    broker = "54.212.20.15"
    mqtt_port = 1883
    estop_ip = "192.168.0.103"

    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.left_motor_command = MotorCommand(
            self.udp_socket, "192.168.0.102", 8888, 4000
        )
        self.right_motor_command = MotorCommand(
            self.udp_socket, "192.168.0.101", 8888, 4000
        )


def main():
    MqttEndPoint()


if __name__ == "__main__":
    main()
