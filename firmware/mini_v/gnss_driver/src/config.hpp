#ifndef __CONFIG_HPP__
#define __CONFIG_HPP__


// self
byte MAC[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED};
const IPAddress IP(192, 168, 0, 100);
const unsigned int LOCALPORT_GNSS = 8888;
const unsigned int LOCALPORT_IMU = 8889;

// destination
const IPAddress IP_DIST(192, 168, 0, 50);
const unsigned int LOCALPORT_GNSS_DIST = 5000;
const unsigned int LOCALPORT_IMU_DIST = 5001;

#endif