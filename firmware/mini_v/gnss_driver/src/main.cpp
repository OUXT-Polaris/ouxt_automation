/**
 * @file getSensorData.ino
 * @author SeanKwok (shaoxiang@m5stack.com)
 * @brief M5Module GNSS Get Possition Demo.
 * @version 0.1
 * @date 2023-08-31
 *  
 *(´・ω・｀)
 * @Hardwares:M5Module GNSS
 * @Platform Version: Arduino M5Stack Board Manager v2.0.7
 * @Dependent Library:
 * TinyGPSPlus: https://github.com/mikalhart/TinyGPSPlus
 */

#include <Arduino.h>
#include <Ethernet.h>
#include <EthernetUdp.h>

#include <proto/geographic_msgs__GeoPose.pb.h>
#include "pb_encode.h"
#include "module_gnss.hpp"
#include "config.hpp"

EthernetUDP Udp;
ModuleGnss gps;
 
void setup() {
    Serial.begin(9600);

    Ethernet.init(9);  // configure the CS pin for M5Stack CoreS3-SE

    // start the Ethernet
    Serial.println("asdf");
    Ethernet.begin(MAC, IP);
    Serial.println("asdf");
    
    // Check for Ethernet hardware present
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
        Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
        while (true) {
        delay(1); // do nothing, no point running without Ethernet hardware
        }
    }
    Serial.println("asdf");
    if (Ethernet.linkStatus() == LinkOFF) {
        Serial.println("Ethernet cable is not connected.");
    }
    Serial.println("asdf");
    
    // start UDP
    Udp.begin(LOCALPORT);
}
uint8_t count =0;
void loop()
{
    if (gps.update())
    {
        ModuleGnssData data = gps.get();

        protolink__geographic_msgs__GeoPose_geographic_msgs__GeoPose msg;
        msg.position.latitude = data.latitude.value;
        msg.position.longitude = data.longitude.value;
        msg.position.altitude = data.altitude.value;
        msg.orientation.w = 0.0;
        msg.orientation.x = 0.0;
        msg.orientation.y = 0.0;
        msg.orientation.z = 0.0;

        uint8_t msg_buffer[128];
        size_t msg_length;
        pb_ostream_t stream = pb_ostream_from_buffer(msg_buffer, sizeof(msg_buffer));

        bool result = pb_encode(&stream, protolink__geographic_msgs__GeoPose_geographic_msgs__GeoPose_fields, &msg);
        if (result && stream.bytes_written > 10)
        {
            Udp.beginPacket(IP_DIST, LOCALPORT_DIST);
            Udp.write(msg_buffer, stream.bytes_written);
            Udp.endPacket();

            Serial.printf("written: %d,", stream.bytes_written);
            data.print();
        }
        else Serial.println("Error: encode");
    }
    else
        Serial.println(F("No GPS data received: check wiring"));
}