# reference : https://github.com/osrf/vrx-docker/blob/master/vrx_server/vrx-server/Dockerfile

ARG BASEIMG=npslearninglab/watery_robots:vrx_base
FROM $BASEIMG

SHELL ["/bin/bash", "-c"]

# Set ROS distribution
ARG ROS_DISTRO=humble

# Create workspace
RUN mkdir -p ~/vrx_ws/src

# TODO: restore version tag
RUN git clone --depth 1 -b 2.3.3 https://github.com/osrf/vrx.git \
&& mv ./vrx ~/vrx_ws/src

# Compile the VRX project.
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && cd ~/vrx_ws && colcon build

## END OF SECTION BASED ON vrx/docker/Dockerfile

# Cache fuel resources
# RUN /bin/bash -c 'gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/sydney_regatta \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/post \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/ground_station \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/antenna \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/mb_marker_buoy_red \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/mb_marker_buoy_black \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/mb_marker_buoy_green \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/mb_marker_buoy_white \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/mb_round_buoy_orange \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/mb_round_buoy_black \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/platypus \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/crocodile \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/turtle \
#   && gz fuel download -u https://fuel.gazebosim.org/1.0/openrobotics/models/wam-v'
ADD fuel.gazebosim.org /root/.gz/fuel/fuel.gazebosim.org

# read wam-v sensors and thruster config
COPY config /home/config

# Expose port used to communiate with gzserver
EXPOSE 11345

# setup entrypoint
RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    source ~/vrx_ws/install/local_setup.bash && \
    ros2 launch vrx_gazebo generate_wamv.launch.py component_yaml:=/home/config/component_config.yaml thruster_yaml:=/home/config/thruster_config.yaml wamv_target:=/home/config/wamv_target.urdf wamv_locked:=False

ADD entrypoint.sh /
RUN chmod +x entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
