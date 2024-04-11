# Run with VRX
[Documents](https://github.com/osrf/vrx/wiki/tutorials)

## How to run demo
### Confirm dependencies
- Docker: a container management tool
- Nvidia-toolkit: Nvidia's software for enabling GPU support from Docker images.
- Rocker: a Docker wrapper that will help build and run your Docker image so it is correctly configured for your local hardware.
  
### Run the vrx simulator and lauch vrx simulation
```
docker run --pull always --net=host --ipc=host --pid=host -it wamvtan/vrx:latest ros2 launch vrx_gz competition.launch.py world:=stationkeeping_task headless:=true urdf:=/home/config/wamv_target.urdf
```
you can change ```world:=``` for your purpose.

If you want to use cuda acceleration, please use this command.

```
docker run --gpus all --pull always --net=host --ipc=host --pid=host -it wamvtan/vrx:latest_cuda ros2 launch vrx_gz competition.launch.py world:=stationkeeping_task headless:=true urdf:=/home/config/wamv_target.urdf
```

### Run vrx_bridgup launch
- [vrx_bridge_node](https://github.com/OUXT-Polaris/vrx_bridge) exchange GNSS topic and Imu topic from vrx to localization system.
Also, vrx recieves [thruster and pose of thruster command](https://github.com/osrf/vrx/wiki/custom_thrusters_tutorial) through vrx_bridge 
- The ekf.lauch commands [geographic_conversion](https://github.com/OUXT-Polaris/geographic_conversion)(geopose_converter_component) and [robotx_ekf_component](https://github.com/OUXT-Polaris/robotx_ekf).   

```
ros2 launch vrx_bridge vrx_bringup.launch.xml
```
