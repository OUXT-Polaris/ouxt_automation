#include <pb_decode.h>

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
        int num_bytes = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
        pb_istream_t pb_stream = pb_istream_from_buffer(packetBuffer, num_bytes);
        pb_decode(&pb_stream, protolink__hardware_communication_msgs__GroundStationHeartBeat_hardware_communication_msgs__GroundStationHeartBeat_fields, &msg);
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

protolink__hardware_communication_msgs__GroundStationHeartBeat_hardware_communication_msgs__GroundStationHeartBeat UDPHeartBeat::get_msgs()
{
    return msg;
}

uint64_t UDPHeartBeat::get_sequence()
{
    return msg.sequence;
}

uint8_t UDPHeartBeat::get_mode()
{
    return msg.mode;
}