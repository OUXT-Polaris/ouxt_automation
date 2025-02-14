#ifndef __CONFIG_HPP__
#define __CONFIG_HPP__

#ifdef RIGHT
byte MAC[] = {
    0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAB
};
const IPAddress IP(192, 168, 0, 101);
const unsigned int LOCALPORT = 8888;  // local port to listen on
#endif

#ifdef LEFT
byte MAC[] = {
    0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAC
};
const IPAddress IP(192, 168, 0, 102);
const unsigned int LOCALPORT = 8888;
#endif

#endif