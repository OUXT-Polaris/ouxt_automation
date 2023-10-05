# generate wamv_target.urdf
ros2 launch vrx_gazebo generate_wamv.launch.py component_yaml:=/home/config/component_config.yaml thruster_yaml:=/home/config/thruster_config.yaml wamv_target:=/home/config/wamv_target.urdf wamv_locked:=False

# launch vrx gazebo
ros2 launch vrx_gz competition.launch.py world:=sydney_regatta headless:=true urdf:=/home/config/wamv_target.urdf