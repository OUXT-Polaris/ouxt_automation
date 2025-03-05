#include <Arduino.h>
#include <NativeEthernet.h>
#include <NativeEthernetUdp.h>
#include <Servo.h>

#include <proto/hardware_communication_msgs__MotorControl.pb.h>
#include "config.hpp"
#include "proto_udp.hpp"


// EStop settings
byte estopPin = 40;
bool preEstopState = true;
unsigned long preTime = 0;

// ESC settings
byte servoPin = 41;
unsigned int startupTime = 4000;
Servo servo;

// Motor Control
ProtoUDP<protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl,
  protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_fields>
    motor_man(LOCALPORT_MOTOR_MAN),
    motor_auto(LOCALPORT_MOTOR_AUTO);


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
  motor_man.begin();
  motor_auto.begin();
  

  // visualize
  digitalWrite(13, HIGH);

  preTime = millis();
}

void loop() {
  bool estopState = !digitalRead(estopPin);      // Estop: true, normal: false

  if (!estopState && preEstopState) {          // When the Estop was released
    preTime = millis();
    servo.writeMicroseconds(1500);
  }
  else if(millis() - preTime > startupTime) {  // delay to allow the ESC to recognize the stopped signal
    protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl msg 
      = protolink__hardware_communication_msgs__MotorControl_hardware_communication_msgs__MotorControl_init_zero;
    
    // Get msg
    bool status = false;
    if (motor_man.get_msg(&msg)) {
      Serial.printf("mode: %d\n", msg.mode);
      status = true;
      if (msg.mode == 0) status = motor_auto.get_msg(&msg);
      else if (msg.mode == 2) msg.motor_enable = false;
    }

    if(status) {
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

  preEstopState = estopState;
  delay(26);
}
