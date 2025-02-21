#include <Arduino.h>
<<<<<<< HEAD
#include <Servo.h>
#include <proto/hardware_communication_msgs__MotorControl.pb.h>
#include "pb_encode.h"
#include "pb_decode.h"
#include <NativeEthernet.h>
#include <NativeEthernetUdp.h>

byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 1, 100);
unsigned int localPort = 8888;      // local port to listen on
// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;
=======
#include <NativeEthernet.h>
#include <NativeEthernetUdp.h>
#include <Servo.h>

#include <proto/hardware_communication_msgs__MotorControl.pb.h>
#include "pb_encode.h"
#include "pb_decode.h"
#include "config.hpp"
#include "heart_beat.hpp"


// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP UdpMotor;
>>>>>>> e6e99620788d4244a48300a042935bab1c4fb7fc

// buffers for receiving and sending data
uint8_t packetBuffer[UDP_TX_PACKET_MAX_SIZE];  // buffer to hold incoming packet,

<<<<<<< HEAD
byte servoPin = 41;
Servo servo;

void setup() {
	servo.attach(servoPin);

	servo.writeMicroseconds(1500); // send "stop" signal to ESC.

	delay(7000); // delay to allow the ESC to recognize the stopped signal

  Ethernet.begin(mac, ip);
=======
// EStop settings
byte estopPin = 40;
bool preEstopState = true;
unsigned long preTime = 0;

// ESC settings
byte servoPin = 41;
unsigned int startupTime = 4000;
Servo servo;

// Heart Beat
UDPHeartBeat UdpHeart(LOCALPORT_HEART, TIMEOUT);


bool get_motor_msg_udp(protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl *msg_) {
  int packetSize = UdpMotor.parsePacket();
  if (packetSize) {
    const size_t num_bytes = UdpMotor.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
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
>>>>>>> e6e99620788d4244a48300a042935bab1c4fb7fc
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
<<<<<<< HEAD
  Udp.begin(localPort);

}

void loop() {
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    const size_t num_bytes = Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);
    pb_istream_t pb_stream = pb_istream_from_buffer(packetBuffer, num_bytes);
    protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl msg 
      = protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_init_zero;
    if(pb_decode(&pb_stream, protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_fields, &msg)) {
      int signal = (int)(constrain(msg.motor_speed, -1.0, 1.0) * 400.0 + 1500.0);
      servo.writeMicroseconds(constrain(signal, 1100, 1900));
    }
  }
=======
  UdpHeart.begin();
  UdpMotor.begin(LOCALPORT_MOTOR);
  

  // visualize
  digitalWrite(13, HIGH);

  preTime = millis();
}

void loop() {
  bool estopState = !digitalRead(estopPin);    // Estop: true, normal: false

  if (UdpHeart.verify_survival()) {              // Check Heart Beat
    if (!estopState && preEstopState) {          // When the Estop was released
      preTime = millis();
      servo.writeMicroseconds(1500);
    }
    else if(millis() - preTime > startupTime) {  // delay to allow the ESC to recognize the stopped signal
      protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl msg 
        = protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_init_zero;
      if(get_motor_msg_udp(&msg)) {
        if (msg.motor_enable && !estopState){
          int signal = (int)(constrain(msg.motor_speed, -1.0, 1.0) * 400.0 + 1500.0);
          servo.writeMicroseconds(constrain(signal, 1100, 1900));
          digitalWrite(13, HIGH);
          Serial.println(signal);
        }
        else{
          servo.writeMicroseconds(1500);
          digitalWrite(13, LOW);
          Serial.println(1500);
        }
      }
    }
    else
      Serial.printf("[%d]: Waiting for starting up\n", millis() - preTime);
  }
  else {
    servo.writeMicroseconds(1500);
    digitalWrite(13, LOW);
    Serial.println("Heart beat is not coming. Stop motor.");
  }

  preEstopState = estopState;
  delay(1);
>>>>>>> e6e99620788d4244a48300a042935bab1c4fb7fc
}
