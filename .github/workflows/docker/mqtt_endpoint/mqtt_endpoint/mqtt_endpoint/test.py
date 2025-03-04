import time
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)
import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command = hardware_communication_msgs__MotorControl()
    command.motor_enable = True
    command.motor_speed = 0.3
    command.mode = 1
    while True:
        udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(command),
            ("192.168.0.102", 8888),
        )
        udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(command),
            ("192.168.0.101", 8888),
        )
        time.sleep(0.1)
