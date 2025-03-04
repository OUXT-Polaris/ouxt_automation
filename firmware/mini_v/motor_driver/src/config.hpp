#ifndef __CONFIG_HPP__
#define __CONFIG_HPP__


const unsigned long TIMEOUT = 1000;

#ifdef RIGHT
byte MAC[] = {
    0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAB
};
const IPAddress IP(192, 168, 0, 101);
const unsigned int LOCALPORT_MOTOR_MAN = 8888;  // local port to listen on
const unsigned int LOCALPORT_MOTOR_AUTO = 8889;  // local port to listen on
const unsigned int LOCALPORT_HEART = 4000;  // local port to listen on
#endif

#ifdef LEFT
byte MAC[] = {
    0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAC
};
const IPAddress IP(192, 168, 0, 102);
const unsigned int LOCALPORT_MOTOR_MAN = 8888;  // local port to listen on
const unsigned int LOCALPORT_MOTOR_AUTO = 8889;  // local port to listen on
const unsigned int LOCALPORT_HEART = 4000;  // local port to listen on
#endif

#endif