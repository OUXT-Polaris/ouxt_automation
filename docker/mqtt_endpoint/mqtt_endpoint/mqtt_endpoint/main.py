import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.hardware_communication_msgs__HeartBeat_pb2 import (
    hardware_communication_msgs__HeartBeat,
)


def main():
    broker = "54.212.20.15"
    port = 1883
    topic = "miniv/heartbeat"
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    client = mqtt.Client()

    client.connect(broker, port)
    sequence = 0
    message = hardware_communication_msgs__HeartBeat
    while True:
        if client.is_connected():
            print("Send heart beat to EStop")
            print("message.SerializeToString()")
            message.sequence = sequence
            sequence = sequence + 1
            sock.sendto(message.SerializeToString(), (broadcast_ip, port))
        else:
            print("Does not connected")
        # message = "Hello, MQTT!"
        # print(f"Sending message: {message}")
        # client.publish(topic, message)
        time.sleep(1)


if __name__ == "__main__":
    main()
