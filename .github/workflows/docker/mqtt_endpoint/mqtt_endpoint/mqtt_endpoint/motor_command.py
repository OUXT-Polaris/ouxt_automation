import time
import socket
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)
from google.protobuf.json_format import MessageToJson


class MotorCommand:
    def __init__(
        self,
        ip_address: str,
        command_port: int,
        command_topic: str,
    ):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 0)
        self.command: hardware_communication_msgs__MotorControl = (
            hardware_communication_msgs__MotorControl()
        )
        self.stop = False
        self.command.motor_enable = True
        self.command.mode = 1
        self.ip_address = ip_address
        self.command_port = command_port
        self.command_topic = command_topic

    def set_mode(self, mode: int):
        self.command.mode = mode

    def send_command(self):
        # print(MessageToJson(self.command))
        self.udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(self.command),
            (self.ip_address, self.command_port),
        )

    def send_command_from_serialized_string(self, serialized_string: str):
        self.command.ParseFromString(serialized_string)
        # print(MessageToJson(self.command))
        self.send_command()
