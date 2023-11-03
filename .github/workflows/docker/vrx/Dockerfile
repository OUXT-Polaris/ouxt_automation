# reference : https://github.com/osrf/vrx-docker/blob/master/vrx_server/vrx-server/Dockerfile

ARG BASEIMG=npslearninglab/watery_robots:vrx_base
FROM $BASEIMG

# Set ROS distribution
ARG ROSDIST=humble

# Create workspace
RUN mkdir -p ~/vrx_ws/src

# TODO: restore version tag
RUN git clone --depth 1 -b 2.3.3 https://github.com/osrf/vrx.git \
&& mv ./vrx ~/vrx_ws/src

# Compile the VRX project.
RUN /bin/bash -c ". /opt/ros/${ROSDIST}/setup.bash && cd ~/vrx_ws && colcon build --merge-install"

# Source all the needed environment files.
RUN /bin/sh -c 'echo ". /opt/ros/${ROSDIST}/setup.bash" >> ~/.bashrc' \
 && /bin/sh -c 'echo ". ~/vrx_ws/install/setup.sh" >> ~/.bashrc'
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

RUN git clone https://github.com/OUXT-Polaris/ouxt_automation.git \
&& mv ./ouxt_automation ~/ouxt_automation
WORKDIR ~/ouxt_automation
RUN sh setup.sh

RUN /bin/sh -c 'echo ". ~/ouxt_automation/install/local_setup.bash" >> ~/.bashrc'

WORKDIR /
# setup entrypoint
COPY ./vrx_entrypoint.sh /

COPY ./run_vrx_gazebo.bash /

ENTRYPOINT ["/vrx_entrypoint.sh"]
