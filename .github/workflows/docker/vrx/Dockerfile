# reference : https://github.com/osrf/vrx-docker/blob/master/vrx_server/vrx-server/Dockerfile

ARG BASEIMG=npslearninglab/watery_robots:vrx_base
FROM $BASEIMG

SHELL ["/bin/bash", "-c"]

# Set ROS distribution
ARG ROS_DISTRO=humble

# Create workspace
RUN mkdir -p ~/vrx_ws/src

# RUN apt-get update && \
#     apt-get upgrade -y && \
#     apt-get install -y libgz-rendering7-ogre2-dev && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/*

# TODO: restore version tag
ADD https://api.github.com/repos/OUXT-Polaris/vrx/git/refs/heads/feature/laser_refrection version.json
RUN git clone --depth 1 -b feature/laser_refrection https://github.com/OUXT-Polaris/vrx.git \
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

ENV GZ_SIM_RESOURCE_PATH=${GZ_SIM_RESOURCE_PATH}:/root/vrx_ws/install/wamv_description/share:/root/vrx_ws/install/wamv_gazebo/share

ENTRYPOINT ["/entrypoint.sh"]
