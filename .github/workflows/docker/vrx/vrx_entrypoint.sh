#!/bin/bash
set -e

# setup ros environment.
source "/opt/ros/humble/setup.bash" > /dev/null

# setup vrx environment
source ~/vrx_ws/install/setup.sh
source /home/ouxt_automation/robotx_ws/install/local_setup.bash
echo "vrx entrypoint executed"

# TODO: optionally disable this so a gzclient can be run on the host for development.
export GAZEBO_IP=127.0.0.1
export GAZEBO_IP_WHITE_LIST=127.0.0.1

/run_vrx_gazebo.bash
exec "$@"
