#include "heart_beat.hpp"

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