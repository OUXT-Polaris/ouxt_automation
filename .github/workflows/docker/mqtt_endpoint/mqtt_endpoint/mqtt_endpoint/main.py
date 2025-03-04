import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.hardware_communication_msgs__HeartBeat_pb2 import (
    hardware_communication_msgs__HeartBeat,
)
from mqtt_endpoint.hardware_communication_msgs__MotorControl_pb2 import (
    hardware_communication_msgs__MotorControl,
)
from google.protobuf.json_format import MessageToJson

heartbeat_topic = "miniv/heartbeat"
lwt_topic = "client/status"
lwt_message = "Remote motor control command disconnected"
left_motor_control_topic = "miniv/left_motor"
left_motor_command = hardware_communication_msgs__MotorControl()
left_motor_command.motor_enable = True
right_motor_control_topic = "miniv/right_motor"
right_motor_command = hardware_communication_msgs__MotorControl()
right_motor_command.motor_enable = True
disconnection_count = 0

right_motor_ip = "192.168.0.101"
left_motor_ip = "192.168.0.102"

udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        # Subscribe all topics
        client.subscribe("#")
    else:
        print(f"Connection failed with code {rc}")


def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Unexpected disconnection. Reconnecting... (rc={rc})")
        time.sleep(5)
        try:
            client.reconnect()
        except Exception as e:
            print(f"Reconnection failed: {e}")


def on_message(client, userdata, msg):
    if msg.topic == left_motor_control_topic:
        left_motor_command.ParseFromString(msg.payload)
    if msg.topic == right_motor_control_topic:
        right_motor_command.ParseFromString(msg.payload)
    if msg.topic == lwt_topic and msg.payload == lwt_message:
        print("Motor control command disconnected")
    udp_sock.sendto(
        hardware_communication_msgs__HeartBeat.SerializeToString(left_motor_command),
        (left_motor_ip, 8888),
    )
    udp_sock.sendto(
        hardware_communication_msgs__HeartBeat.SerializeToString(right_motor_command),
        (right_motor_ip, 8888),
    )


def main():
    broker = "54.212.20.15"
    port = 1883
    estop_ip = "192.168.0.103"

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    keep_alive_timeout = 1

    try:
        client.connect(broker, port, keep_alive_timeout)
        client.loop_start()

        sequence = 0
        message = hardware_communication_msgs__HeartBeat()
        time.sleep(1)
        while True:
            if not client.is_connected():
                disconnection_count = disconnection_count + 1
            else:
                disconnection_count = 0
            if disconnection_count >= 3:
                print("Disconnection detected, shuting down...")
                break
            sequence = sequence + 1
            message.sequence = sequence
            # print("Send heart beat to EStop")
            # print(MessageToJson(message))
            udp_sock.sendto(
                hardware_communication_msgs__HeartBeat.SerializeToString(message),
                (estop_ip, 4000),
            )
            udp_sock.sendto(
                hardware_communication_msgs__HeartBeat.SerializeToString(message),
                (left_motor_ip, 4000),
            )
            udp_sock.sendto(
                hardware_communication_msgs__HeartBeat.SerializeToString(message),
                (right_motor_ip, 4000),
            )
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(e)
    finally:
        left_motor_command.motor_speed = 0
        udp_sock.sendto(
            hardware_communication_msgs__HeartBeat.SerializeToString(
                left_motor_command
            ),
            (left_motor_ip, 8888),
        )
        right_motor_command.motor_speed = 0
        udp_sock.sendto(
            hardware_communication_msgs__HeartBeat.SerializeToString(
                right_motor_command
            ),
            (right_motor_ip, 8888),
        )
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
