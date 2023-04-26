FROM nvidia/cuda:12.0.1-base-ubuntu22.04

# register gpg key for ROS2
RUN apt-get update && \
    apt-get install -y locales software-properties-common curl && \
    locale-gen en_US en_US.UTF-8 && \
    update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 && \
    add-apt-repository universe && \
    rm -rf /var/lib/apt/lists/*
ENV LANG en_US.UTF-8
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

# install ros-humble-ros-base/ros-dev-tools/othre tools
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && \
    apt-get install -y ros-humble-ros-base ros-dev-tools git wget && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
RUN apt-get update && apt-get install -y \
    python3-sdformat13 \
    gz-garden \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /home/vrx_ws/src
WORKDIR /home/vrx_ws/src
ADD https://api.github.com/repos/osrf/vrx/git/refs/heads/main vrx_version.json
RUN git clone https://github.com/osrf/vrx.git
ADD https://api.github.com/repos/gazebosim/ros_gz/git/refs/heads/humble ros_gz_version.json
RUN git clone https://github.com/gazebosim/ros_gz.git -b humble
ENV GZ_VERSION garden
WORKDIR /home/vrx_ws
RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.sh && apt-get update && rosdep init && rosdep update && rosdep install -iry --from-paths src && rm -rf /var/lib/apt/lists/*"]
RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.sh && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release"]
ADD fuel.gazebosim.org /root/.gz/fuel/fuel.gazebosim.org
COPY config /home/config
ENV GZ_SIM_RESOURCE_PATH /home/vrx_ws/src/vrx/vrx_urdf:${GZ_SIM_RESOURCE_PATH}
RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash && source /home/vrx_ws/install/local_setup.bash && ros2 launch vrx_gazebo generate_wamv.launch.py component_yaml:=/home/config/component_config.yaml thruster_yaml:=/home/config/thruster_config.yaml wamv_target:=/home/config/wamv_target.urdf wamv_locked:=False"]
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash && source /home/vrx_ws/install/local_setup.bash && ros2 launch vrx_gz competition.launch.py world:=sydney_regatta headless:=true urdf:=/home/config/wamv_target.urdf"]