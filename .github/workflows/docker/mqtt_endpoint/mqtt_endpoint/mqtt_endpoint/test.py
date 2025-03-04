import time
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)
from mqtt_endpoint.ground_station_heartbeat_pb2 import (
    ground_station_heartbeat,
)
import socket


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    command = hardware_communication_msgs__MotorControl()
    command.motor_enable = True
    command.motor_speed = 0.3
    command.mode = 1
    heartbeat_command = ground_station_heartbeat()
    heartbeat_command.sequence = 1
    heartbeat_command.mode = 1
    while True:
        udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(command),
            ("192.168.0.102", 8888),
        )
        udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(command),
            ("192.168.0.101", 8888),
        )
        udp_socket.sendto(
            ground_station_heartbeat.SerializeToString(heartbeat_command),
            ("192.168.0.103", 4000),
        )
        time.sleep(0.1)
