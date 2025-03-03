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
import joy_controller as joy


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

    broker = "54.212.20.15"
    port = 1883
    client = mqtt.Client()

    keep_alive_timeout = 1


    try:
        client.connect(broker, port, keep_alive_timeout)
        client.on_connect = on_connect
        client.loop_start()
        time.sleep(1)

        sequence = 0
        while True:
            if not client.is_connected():
                break

            left_motor_command.motor_speed = joy.get_stick_left_y()
            right_motor_command.motor_speed = joy.get_stick_right_y()
            heartbeat_command.sequence = sequence = sequence + 1 
            heartbeat_command.mode = joy.get_mode()

            client.publish(
                left_motor_control_topic, left_motor_command.SerializeToString()
            )
            client.publish(
                right_motor_control_topic, right_motor_command.SerializeToString()
            )
            # TODO Fill heartbeat topic from joystick button input.
            # if the user press Emergency stop button, fill "EMERGENCY" instead of "AUTO"
            client.publish(groundstation_heartbeat_topic, "AUTO")
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(e)
    finally:
        left_motor_command.motor_speed = 0
        client.publish(left_motor_control_topic, left_motor_command.SerializeToString())
        right_motor_command.motor_speed = 0
        client.publish(
            right_motor_control_topic, right_motor_command.SerializeToString()
        )
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
