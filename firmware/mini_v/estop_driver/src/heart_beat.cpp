#include "heart_beat.hpp"

MqttHeartBeat::MqttHeartBeat(EthernetClient & network) : network(network)
{
    // Setup MqttClient
	MqttClient::System *mqttSystem = new System;
	// MqttClient::Logger *mqttLogger = new MqttClient::LoggerImpl<HardwareSerial>(Serial);
	MqttClient::Network * mqttNetwork = new MqttClient::NetworkClientImpl<Client>(network, *mqttSystem);
	//// Make 128 bytes send buffer
	MqttClient::Buffer *mqttSendBuffer = new MqttClient::ArrayBuffer<128>();
	//// Make 128 bytes receive buffer
	MqttClient::Buffer *mqttRecvBuffer = new MqttClient::ArrayBuffer<128>();
}

void MqttHeartBeat::on_loop()
{
    // Check connection status
	if (!mqtt->isConnected()) {
		// Close connection if exists
		network.stop();
		// Re-establish TCP connection with MQTT broker
		network.connect("test.mosquitto.org", 1883);
		// Start new MQTT connection
		// LOG_PRINTFLN("Connecting");
		MqttClient::ConnectResult connectResult;
		// Connect
		{
			MQTTPacket_connectData options = MQTTPacket_connectData_initializer;
			options.MQTTVersion = 4;
			options.clientID.cstring = "espot";
			options.cleansession = true;
			options.keepAliveInterval = 15; // 15 seconds
			MqttClient::Error::type rc = mqtt->connect(options, connectResult);
			if (rc != MqttClient::Error::SUCCESS) {
				// LOG_PRINTFLN("Connection error: %i", rc);
				return;
			}
		}
		{
			// Add subscribe here if need
		}
	} else {
		{
			// Add publish here if need
		}
		// Idle for 30 seconds
		mqtt->yield(30000L);
	}
}

UDPHeartBeat::UDPHeartBeat(u_int16_t _port, unsigned long _timeout = 1000) : port(_port), timeout(_timeout) {
    
}

void UDPHeartBeat::begin(){
    Udp.begin(port);
}

bool UDPHeartBeat::update_msgs()
{
    int packetSize = Udp.parsePacket();
    if (packetSize) {
        Serial.print("Received packet of size ");
        Serial.print(packetSize);
        Serial.print("  From ");
        IPAddress remote = Udp.remoteIP();
        for (int i=0; i < 4; i++) {
        Serial.print(remote[i], DEC);
        if (i < 3) Serial.print(".");
        }
        Serial.print(", port ");
        Serial.print(Udp.remotePort());
        Serial.print(" heart");
        const size_t num_bytes = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
        
        for (auto c : packetBuffer){
            Serial.print(" ");
            Serial.print(c);
        }
        Serial.println();
        return true;
    }
    return false;
}

bool UDPHeartBeat::verify_survival()
{
    if (update_msgs()) {
        preTime = millis();
        return true;
    }
    else if (timeout > millis() - preTime) {
        return true;
    }
    return false;
}

protolink__hardware_communication_msgs__HeartBeat_hardware_communication_msgs__HeartBeat UDPHeartBeat::get_msgs()
{
    return msg;
}
