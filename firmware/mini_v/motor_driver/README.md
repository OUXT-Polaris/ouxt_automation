# motor_driver

Farmware to control the mini-V's two thrusters.

## Enviroments
- Hardware
  - Teensy4.1
  - Ethernet adapter
  - LAN cable
- Software
  - ROS2
  - Protolink (Nanopb)
  - Platform IO

## Description

Use Teensy for each of the two thrusters(right and left).
IP and Port settings are in src/config.hpp.
Both right and left settings are described,
but they are switched and build by macros and build flags. <br>
Please specify the appropriate Platform IO environment( env:right or env:left ) when building and uploading.