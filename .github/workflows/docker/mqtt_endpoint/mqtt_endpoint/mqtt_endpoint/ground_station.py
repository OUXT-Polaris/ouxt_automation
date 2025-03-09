# Todo Get Joystick input by pygame
import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)
from mqtt_endpoint.ground_station_heartbeat_pb2 import (
    ground_station_heartbeat,
)
from mqtt_endpoint.joy_controller import JoyController
from google.protobuf.json_format import MessageToJson


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Connection failed with code {rc}")


def main():
    left_motor_control_topic = "miniv/left_motor"
    left_motor_command = hardware_communication_msgs__MotorControl()
    left_motor_command.motor_enable = True

    right_motor_control_topic = "miniv/right_motor"
    right_motor_command = hardware_communication_msgs__MotorControl()
    right_motor_command.motor_enable = True

    groundstation_heartbeat_topic = "ground_station/heartbeat"
    heartbeat_command = ground_station_heartbeat()

    joy_controller = JoyController()

    broker = "54.212.20.15"
    port = 1883
    client = mqtt.Client()

    # keep_alive_timeout = 1

    try:
        client.connect(broker, port)
        client.on_connect = on_connect
        client.loop_start()
        time.sleep(1)

        sequence = 1
        while True:
            if not client.is_connected():
                break
            joy_controller.update()
            left_motor_command.motor_speed = joy_controller.stick_ly
            right_motor_command.motor_speed = joy_controller.stick_ry
            heartbeat_command.sequence = sequence
            sequence = sequence + 1
            heartbeat_command.mode = joy_controller.mode
            right_motor_command.mode = joy_controller.mode
            left_motor_command.mode = joy_controller.mode
            # if heartbeat_command.mode == 0:
            #     print("mode : AUTO")
            # elif heartbeat_command.mode == 1:
            #     print("mode : MANUAL")
            # elif heartbeat_command.mode == 2:
            #     print("mode : ESTOP")
            client.publish(
                left_motor_control_topic, left_motor_command.SerializeToString(), qos=0
            )
            client.publish(
                right_motor_control_topic,
                right_motor_command.SerializeToString(),
                qos=0,
            )
            client.publish(
                groundstation_heartbeat_topic,
                heartbeat_command.SerializeToString(),
                qos=0,
            )
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(e)
    finally:
        left_motor_command.motor_speed = 0
        client.publish(
            left_motor_control_topic, left_motor_command.SerializeToString(), qos=0
        )
        right_motor_command.motor_speed = 0
        client.publish(
            right_motor_control_topic, right_motor_command.SerializeToString(), qos=0
        )
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
