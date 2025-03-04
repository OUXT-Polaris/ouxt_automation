import time
import socket
import sched
from mqtt_endpoint.ground_station_heartbeat_pb2 import ground_station_heartbeat
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)


class MotorCommand:
    def __init__(
        self,
        udp_socket,
        ip_address: str,
        command_port: int,
        heartbeat_port: int,
        command_topic: str,
        scheduler: sched.scheduler,
    ):
        self.command: hardware_communication_msgs__MotorControl = (
            hardware_communication_msgs__MotorControl()
        )
        self.heartbeat: ground_station_heartbeat = ground_station_heartbeat()
        self.heartbeat.sequence = 1
        self.heartbeat.mode = 1
        self.stop = False
        self.command.motor_enable = True
        self.udp_socket = udp_socket
        self.ip_address = ip_address
        self.command_port = command_port
        self.heartbeat_port = heartbeat_port
        self.command_topic = command_topic
        self.scheduler = scheduler
        self.send_heartbeat(self.scheduler)

    def set_mode(self, mode: int):
        self.heartbeat.mode = mode

    def send_command(self):
        self.udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(self.command),
            (self.ip_address, self.command_port),
        )

    def send_heartbeat(self, scheduler):
        self.heartbeat.sequence = self.heartbeat.sequence + 1
        if not self.stop:
            self.udp_socket.sendto(
                ground_station_heartbeat.SerializeToString(self.heartbeat),
                (self.ip_address, self.heartbeat_port),
            )
        else:
            print("Try stopping motor")
            self.command.motor_speed = 0
            self.send()
        scheduler.enter(0.1, 1, self.send_heartbeat, (scheduler,))

    def send_command_from_serialized_string(self, serialized_string: str):
        if not self.stop:
            self.command.ParseFromString(serialized_string)
            self.send_command()
        else:
            self.command.motor_speed = 0
            self.send_command()
