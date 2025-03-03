#include "heart_beat.hpp"

MqttHeartBeat::MqttHeartBeat(EthernetClient & network, const std::string & broker_url) 
: network(network), 
  broker_url(broker_url)
{
    // Setup MqttClient
	mqttSystem = new System;
	// MqttClient::Logger *mqttLogger = new MqttClient::LoggerImpl<HardwareSerial>(Serial);
	mqttNetwork = new MqttClient::NetworkClientImpl<Client>(network, *mqttSystem);
	//// Make 128 bytes send buffer
	mqttSendBuffer = new MqttClient::ArrayBuffer<128>();
	//// Make 128 bytes receive buffer
	mqttRecvBuffer = new MqttClient::ArrayBuffer<128>();
}

auto MqttHeartBeat::is_connected() -> bool
{
    return mqtt->isConnected();
}

auto MqttHeartBeat::reconnect() -> void
{
    if(is_connected()) {
		// Close connection if exists
		network.stop();
		// Re-establish TCP connection with MQTT broker
		network.connect(broker_url.c_str(), 1883);
		// Start new MQTT connection
		// LOG_PRINTFLN("Connecting");
		MqttClient::ConnectResult connectResult;
		// Connect
		{
			MQTTPacket_connectData options = MQTTPacket_connectData_initializer;
			options.MQTTVersion = 4;
			options.clientID.cstring = "estop";
			options.cleansession = true;
			options.keepAliveInterval = 15; // 15 seconds
			MqttClient::Error::type rc = mqtt->connect(options, connectResult);
			if (rc != MqttClient::Error::SUCCESS) {
				// LOG_PRINTFLN("Connection error: %i", rc);
				return;
			}
		}
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
