import socket
import time

from mqtt_endpoint.ground_station_heartbeat_pb2 import ground_station_heartbeat
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import \
    hardware_communication_msgs__MotorControl
from mqtt_endpoint.joy_controller import JoyController


def on_message(client, userdata, msg):
    pass


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    command_l = hardware_communication_msgs__MotorControl()
    command_r = hardware_communication_msgs__MotorControl()
    command_l.motor_enable = True
    command_r.motor_enable = True

    heartbeat_command = ground_station_heartbeat()
    sequence = 1

    joy_controller = JoyController()

    while True:
        joy_controller.update()

        command_l.motor_speed = joy_controller.stick_ly
        command_r.motor_speed = joy_controller.stick_ry

        command_l.mode = joy_controller.mode
        command_r.mode = joy_controller.mode

        heartbeat_command.sequence = sequence = sequence + 1
        heartbeat_command.mode = joy_controller.mode

        print(
            f"i: {sequence}, msr: {command_r.motor_speed}, msl: {command_l.motor_speed}, mr: {command_r.mode}, ml: {command_l.mode}"
        )
        udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(command_r),
            ("192.168.1.200", 9001),
        )
        udp_socket.sendto(
            hardware_communication_msgs__MotorControl.SerializeToString(command_l),
            ("192.168.1.200", 9002),
        )
        udp_socket.sendto(
            ground_station_heartbeat.SerializeToString(heartbeat_command),
            ("192.168.1.200", 9003),
        )
        time.sleep(0.1)
