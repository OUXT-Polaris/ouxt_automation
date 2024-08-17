#!/bin/bash
set -e

source "/opt/ros/humble/setup.bash"
source /wamv_ws/install/setup.sh

exec "$@"
