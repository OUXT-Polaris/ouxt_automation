import time
import socket
import sched
from mqtt_endpoint.hardware_communication_msgs__HeartBeat_pb2 import (
    hardware_communication_msgs__HeartBeat,
)
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)


class MotorCommand:
    def __init__(
        self, udp_socket, ip_address: str, command_port: int, heartbeat_port: int
    ):
        self.command: hardware_communication_msgs__MotorControl = (
            hardware_communication_msgs__MotorControl()
        )
        self.command.motor_enable = True
        self.udp_socket = udp_socket
        self.ip_address = ip_address
        self.command_port = command_port
        self.heartbeat_port = heartbeat_port
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.send_heartbeat(self.scheduler)
        self.scheduler.run()

    def send(self, motor_speed: float):
        self.udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(self.command),
            (self.ip_address, self.command_port),
        )

    def send_heartbeat(self, scheduler):
        self.udp_socket.sendto(
            hardware_communication_msgs__HeartBeat.SerializeToString(self.command),
            (self.ip_address, self.heartbeat_port),
        )
        scheduler.enter(0.1, 1, self.send_heartbeat, (scheduler,))
