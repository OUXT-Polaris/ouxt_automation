#!/bin/bash
set -e

# setup ros environment.
source "/opt/ros/$ROS_DISTRO/setup.bash"

# exec "$@"

# record all topics
ros2 bag record -a -d 10 -s mcap -o /rosbag
