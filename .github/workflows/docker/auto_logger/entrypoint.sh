#!/bin/bash
set -e

ls /config

# setup ros environment.
# source "/opt/ros/$ROS_DISTRO/setup.bash"

# record all topics
# ros2 bag record -d 10 -s mcap --storage-config-file ./settings/storage_options.yaml $(cat /config/topic.txt)
