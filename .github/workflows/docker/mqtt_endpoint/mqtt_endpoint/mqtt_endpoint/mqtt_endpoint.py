import time
import socket
import sched
import paho.mqtt.client as mqtt
from mqtt_endpoint.hardware_communication_msgs__HeartBeat_pb2 import (
    hardware_communication_msgs__HeartBeat,
)
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)


class MotorCommand:
    command: hardware_communication_msgs__MotorControl = (
        hardware_communication_msgs__MotorControl()
    )
    ip_address: str
    command_port: int
    heartbeat_port: int
    udp_socket

    def __init__(
        self, udp_socket, ip_address: str, command_port: int, heartbeat_port: int
    ):
        command.motor_enable = True
        self.udp_socket = udp_socket
        self.ip_address = ip_address
        self.command_port = command_port
        self.heartbeat_port = heartbeat_port
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.send_heartbeat(self.scheduler)
        self.scheduler.run()

    def send(self, motor_speed: double):
        self.udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(self.command),
            (self.ip_address, self.command_port),
        )

    def send_heartbeat(self, scheduler):
        self.udp_socket.sendto(
            hardware_communication_msgs__HeartBeat.SerializeToString(self.command),
            (self.ip_address, self.heartbeat_port),
        )
        scheduler.enter(0.1, 1, self.task, (scheduler,))


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

    udp_socket
    left_motor_command: MotorCommand
    right_motor_command: MotorCommand

    def __init__(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.left_motor_command = MotorCommand(
            self.udp_socket, "192.168.0.102", 8888, 4000
        )
        self.right_motor_command = MotorCommand(
            self.udp_socket, "192.168.0.101", 8888, 4000
        )


if __name__ == "__main__":
    pass
