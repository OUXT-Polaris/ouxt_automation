import time
import socket
import paho.mqtt.client as mqtt
from mqtt_endpoint.hardware_communication_msgs__HeartBeat_pb2 import (
    hardware_communication_msgs__HeartBeat,
)
from google.protobuf.json_format import MessageToJson

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
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


def main():
    broker = "54.212.20.15"
    port = 1883
    topic = "miniv/heartbeat"
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    try:
        client.connect(broker, port, 1)
        client.loop_start()

        sequence = 0
        message = hardware_communication_msgs__HeartBeat()
        time.sleep(3)
        while True:
            if not client.is_connected():
                break
            sequence = sequence + 1
            message.sequence = sequence
            print("Send heart beat to EStop")
            print(MessageToJson(message))
            udp_sock.sendto(
                hardware_communication_msgs__HeartBeat.SerializeToString(message),
                ("192.168.0.103", 4000),
            )
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    except Exception as e:
        print(e)
    finally:
        client.loop_stop()
        client.disconnect()


if __name__ == "__main__":
    main()
