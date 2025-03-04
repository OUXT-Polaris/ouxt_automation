#ifndef __PROTO_UDP_HPP__
#define __PROTO_UDP_HPP__


#include <NativeEthernet.h>
#include <NativeEthernetUdp.h>

#include <pb.h>
#include <pb_decode.h>

template <typename T, const pb_msgdesc_t* F>
class ProtoUDP {
public:
    ProtoUDP(uint16_t _port) : port(_port) {};
    void begin()
    {
        Udp.begin(port);
    };  // After define Ethernet.begin

    bool get_msg(T *msg_) {
        int packetSize = Udp.parsePacket();
        if (packetSize) {
          int num_bytes = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
          pb_istream_t pb_stream = pb_istream_from_buffer(packetBuffer, num_bytes);
          return pb_decode(&pb_stream, msg_fiels, msg_);
        }
        return false;
    };

    bool flush() {
        int packetSize = Udp.parsePacket();
        if (packetSize) {
            int num_bytes = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);

            if (num_bytes == packetSize) return true;
        }
        return false;
    };

private:
    const uint16_t port;
    const pb_msgdesc_t* msg_fiels = F;
    
    EthernetUDP Udp;
    uint8_t packetBuffer[UDP_TX_PACKET_MAX_SIZE];  // buffer to hold incoming packet,
};

#endif