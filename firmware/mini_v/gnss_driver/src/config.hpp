#ifndef __CONFIG_HPP__
#define __CONFIG_HPP__


// self
byte MAC[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
const IPAddress IP(192, 168, 0, 100);
const unsigned int LOCALPORT = 8888;

// destination
const IPAddress IP_DIST(192, 168, 0, 200);
const unsigned int LOCALPORT_DIST = 5000;

#endif