import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
    else:
        print(f"Connection failed with code {rc}")

def main():
    left_motor_control_topic = "miniv/left_motor"
    left_motor_command = hardware_communication_msgs__MotorControl()
    left_motor_command.motor_enable = True
    left_motor_command.motor_speed = 0.3
    right_motor_control_topic = "miniv/right_motor"
    right_motor_command = hardware_communication_msgs__MotorControl()
    right_motor_command.motor_enable = True
    right_motor_command.motor_speed = 0.3

    broker = "54.212.20.15"
    port = 1883
    client = mqtt.Client()

    keep_alive_timeout = 1

    try:
        client.connect(broker, port, keep_alive_timeout)
        client.on_connect = on_connect
        client.loop_start()
        time.sleep(1)
        while True:
            if not client.is_connected():
                break
            client.publish(
                left_motor_control_topic, left_motor_command.SerializeToString()
            )
            client.publish(
                right_motor_control_topic, right_motor_command.SerializeToString()
            )
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(e)
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
