#ifndef __HEART_BEAT_HPP__
#define __HEART_BEAT_HPP__


#include <NativeEthernet.h>
#include <NativeEthernetUdp.h>

#include "proto/hardware_communication_msgs__GroundStationHeartBeat.pb.h"
#include "pb_decode.h"


class UDPHeartBeat {
public:
    UDPHeartBeat(uint16_t port, unsigned long timeout);
    void begin();  // After define Ethernet.begin

    bool verify_survival();
    
    auto get_msgs() -> protolink__hardware_communication_msgs__GroundStationHeartBeat_hardware_communication_msgs__GroundStationHeartBeat;
    uint64_t get_sequence();
    uint8_t get_mode();

private:
    const uint16_t port;
    EthernetUDP Udp;
    uint8_t packetBuffer[UDP_TX_PACKET_MAX_SIZE];  // buffer to hold incoming packet,

    protolink__hardware_communication_msgs__GroundStationHeartBeat_hardware_communication_msgs__GroundStationHeartBeat msg
     = protolink__hardware_communication_msgs__GroundStationHeartBeat_hardware_communication_msgs__GroundStationHeartBeat_init_zero;

    unsigned long preTime = 0;
    unsigned long timeout;  // ms


    bool update_msgs();
};

#endif
