#include <Arduino.h>
#include <Ethernet.h>
#include <EthernetUdp.h>
#include <M5Unified.h>

#include <proto/geographic_msgs__GeoPose.pb.h>
#include "pb_encode.h"
#include "module_gnss.hpp"
#include "config.hpp"

EthernetUDP Udp;
ModuleGnss gps;


void m5print(String text, int x = 0, int y = 10)
{
    M5.Lcd.setTextSize(2);
    M5.Lcd.setCursor(x, y);
    M5.Lcd.print(text);
}

void print_cood(double lat, double lng, double alt)
{
    char c[50];
    snprintf(c, 50, "%f", lat); m5print(c, 0, 60);
    snprintf(c, 50, "%f", lng); m5print(c, 0, 80);
    snprintf(c, 50, "%f", alt); m5print(c, 0, 100);
}

 
void setup() {
    Serial.begin(9600);

    // start M5 system
    auto cfg = M5.config();
    cfg.clear_display = true;
    M5.begin(cfg);

    Ethernet.init(9);  // configure the CS pin for M5Stack CoreS3-SE

    // start the Ethernet
    Ethernet.begin(MAC, IP);
    
    // Check for Ethernet hardware present
    if (Ethernet.hardwareStatus() == EthernetNoHardware) {
        Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
        while (true) {
        delay(1); // do nothing, no point running without Ethernet hardware
        }
    }

    if (Ethernet.linkStatus() == LinkOFF) {
        Serial.println("Ethernet cable is not connected.");
    }
    
    // start UDP
    Udp.begin(LOCALPORT);
}

void loop()
{
    M5.update();

    if (gps.update())
    {
        ModuleGnssData data = gps.get();
        m5print("GPS data updated!!");
        print_cood(data.latitude.value, data.longitude.value, data.altitude.value);

        protolink__geographic_msgs__GeoPose_geographic_msgs__GeoPose msg 
            = protolink__geographic_msgs__GeoPose_geographic_msgs__GeoPose_init_zero;
        msg.has_position = true;
        msg.has_orientation = true;
        msg.position.latitude = data.latitude.value;
        msg.position.longitude = data.longitude.value;
        msg.position.altitude = data.altitude.value;
        msg.orientation.w = 0.0;
        msg.orientation.x = 0.0;
        msg.orientation.y = 0.0;
        msg.orientation.z = 0.0;

        uint8_t msg_buffer[128];
        size_t msg_length = 128;
        pb_ostream_t stream = pb_ostream_from_buffer(msg_buffer, sizeof(msg_buffer));

        bool result = pb_encode(&stream, protolink__geographic_msgs__GeoPose_geographic_msgs__GeoPose_fields, &msg);
        if (result)
        {
            Udp.beginPacket(IP_DIST, LOCALPORT_DIST);
            Udp.write(msg_buffer, stream.bytes_written);
            Udp.endPacket();

            Serial.printf(" written: %d,", stream.bytes_written);
            m5print(F("written"), 0, 40);
            data.print();
        }
        else {
            Serial.printf(" Encode error\n");
            m5print(F("Encode error"), 0, 40);
        }
    }
    else
    {
        Serial.println(F("No GPS data received: check wiring"));
        m5print(F("No GPS data received"));
    }
}