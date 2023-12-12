# VRX Documents
[Documents](https://github.com/osrf/vrx/wiki/tutorials)

## How to run demo
### Confirm dependencies
- Docker: a container management tool
- Nvidia-toolkit: Nvidia's software for enabling GPU support from Docker images.
- Rocker: a Docker wrapper that will help build and run your Docker image so it is correctly configured for your local hardware.
- 
### run the vrx simulator
```
docker pull wamvtan/vrx:latest
docker build wamvtan/vrx:latest
docker run -it wamvtan/vrx:latest /bin/bash
```
#### on the container,launch the station keeping task
```
ros2 launch vrx_gz competition.launch.py world:=stationkeeping_task headless:=true urdf:=/home/config/wamv_target.urdf
```
you can change ```world:=``` for your purpose.

### run vrx_bridge_node
[vrx_bridge_node](https://github.com/OUXT-Polaris/vrx_bridge) exchange GNSS topic and Imu topic from vrx to localization system.
Also, vrx recieves [thruster and pose of thruster command](https://github.com/osrf/vrx/wiki/custom_thrusters_tutorial) through vrx_bridge 
```
ros2 run vrx_bridge vrx_bridge_node
```

### run the localization launch
This ros2 lauch commands [geographic_conversion](https://github.com/OUXT-Polaris/geographic_conversion)(geopose_converter_component) and [robotx_ekf_component](https://github.com/OUXT-Polaris/robotx_ekf).   
```
ros2 launch robotx_ekf ekf.launch.xml
```
