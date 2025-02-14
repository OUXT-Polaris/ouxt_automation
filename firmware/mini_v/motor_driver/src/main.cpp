#include <Arduino.h>
#include <NativeEthernet.h>
#include <NativeEthernetUdp.h>
#include <Servo.h>

#include <proto/hardware_communication_msgs__MotorControl.pb.h>
#include "pb_encode.h"
#include "pb_decode.h"
#include "config.hpp"


// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

// buffers for receiving and sending data
uint8_t packetBuffer[UDP_TX_PACKET_MAX_SIZE];  // buffer to hold incoming packet,

// EStop settings
byte estopPin = 40;
bool preEstopState = true;
unsigned long preTime = 0;

// ESC settings
byte servoPin = 41;
unsigned int startupTime = 4000;
Servo servo;


bool get_msg_udp(protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl *msg_) {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    const size_t num_bytes = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    pb_istream_t pb_stream = pb_istream_from_buffer(packetBuffer, num_bytes);
    return pb_decode(&pb_stream, protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_fields, msg_);
  }
  return false;
}


void setup() {
  Serial.begin(9600);

  pinMode(13, OUTPUT);
  pinMode(estopPin, INPUT_PULLDOWN);

	servo.attach(servoPin);

  Ethernet.begin(MAC, IP);
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

  // visualize
  digitalWrite(13, HIGH);

  preTime = millis();
}

void loop() {
  bool estopState = !digitalRead(estopPin);   // Estop: true, normal: false

  if (!estopState && preEstopState) {
    preTime = millis();
    servo.writeMicroseconds(1500);             // send "stop" signal to ESC.
  }
  else if(millis() - preTime > startupTime) {  // delay to allow the ESC to recognize the stopped signal
    protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl msg 
      = protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_init_zero;
    if(get_msg_udp(&msg)) {
      if (msg.motor_enable && !estopState){
        int signal = (int)(constrain(msg.motor_speed, -1.0, 1.0) * 400.0 + 1500.0);
        servo.writeMicroseconds(constrain(signal, 1100, 1900));
        Serial.println(signal);
      }
      else{
        servo.writeMicroseconds(1500);
        Serial.println(1500);
      }
    }
  }
  preEstopState = estopState;
  delay(1);
}
