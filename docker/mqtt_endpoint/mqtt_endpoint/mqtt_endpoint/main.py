import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.hardware_communication_msgs__HeartBeat_pb2 import (
    hardware_communication_msgs__HeartBeat,
)
from google.protobuf.json_format import MessageToJson


def main():
    broker = "54.212.20.15"
    port = 1883
    topic = "miniv/heartbeat"
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    client = mqtt.Client()

    client.connect(broker, port)
    client.loop_start()

    sequence = 0
    message = hardware_communication_msgs__HeartBeat()
    time.sleep(1)
    while True:
        if client.is_connected():
            sequence = sequence + 1
            message.sequence = sequence
            print("Send heart beat to EStop")
            print(MessageToJson(message))
            udp_sock.sendto(
                hardware_communication_msgs__HeartBeat.SerializeToString(message),
                ("255.255.255.255", port),
            )
        else:
            print("Does not connected")
        # message = "Hello, MQTT!"
        # print(f"Sending message: {message}")
        # client.publish(topic, message)
        time.sleep(1)


if __name__ == "__main__":
    main()
