# generate wamv_target.urdf
ros2 launch vrx_gazebo generate_wamv.launch.py component_yaml:=/home/config/component_config.yaml thruster_yaml:=/home/config/thruster_config.yaml wamv_target:=/home/config/wamv_target.urdf wamv_locked:=False

# launch nav_sim 
ros2 launch navi_sim navi_sim.launch.py&

# run vrx_bridge node to exchange sensor info with nav_sim
ros2 run vrx_bridge vrx_bridge_node&

# launch vrx gazebo
# ros2 launch vrx_gz competition.launch.py world:=stationkeeping_task headless:=true urdf:=/home/config/wamv_target.urdf
