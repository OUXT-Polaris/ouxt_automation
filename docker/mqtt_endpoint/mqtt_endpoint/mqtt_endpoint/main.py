import time
import paho.mqtt.client as mqtt

def main():
    broker = "54.212.20.15"
    port = 1883
    topic = "miniv/heartbeat"

    client = mqtt.Client()

    client.connect(broker, port)

    while True:
        # if client.is_connected():
        # message = "Hello, MQTT!"
        # print(f"Sending message: {message}")
        # client.publish(topic, message)
        time.sleep(1)

if __name__ == "__main__":
    main()
