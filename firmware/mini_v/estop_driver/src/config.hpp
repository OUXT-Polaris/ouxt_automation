#ifndef __CONFIG_HPP__
#define __CONFIG_HPP__


const unsigned long TIMEOUT = 1000;


byte MAC[] = {
    0xAA, 0xAA, 0xAA, 0xAA, 0xAA, 0xAD
};
const IPAddress IP(192, 168, 0, 103);
const unsigned int LOCALPORT_HEART = 4000;  // local port to listen on


#endif