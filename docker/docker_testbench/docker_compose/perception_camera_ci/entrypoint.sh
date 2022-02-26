#!/bin/bash
exec /bin/bash -l -c "source /opt/ros/galactic/install/setup.bash && colcon build --symlink-install --packages-up-to tensorrt_common"