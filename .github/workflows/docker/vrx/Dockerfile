FROM ros:humble-ros-base
RUN apt-get update && apt-get install -y \
    git \
    python3-vcstool \
    python3-colcon-common-extensions \
    wget \
    && rm -rf /var/lib/apt/lists/*
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
RUN apt-get update
RUN rosdep install -iry --from-paths .
ENV GZ_VERSION garden
WORKDIR /home/vrx_ws
RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.sh && colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release"]
ADD fuel.gazebosim.org /root/.gz/fuel/fuel.gazebosim.org
COPY config /home/config
ENV GZ_SIM_RESOURCE_PATH /home/vrx_ws/src/vrx/vrx_urdf:${GZ_SIM_RESOURCE_PATH}
RUN ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash && source /home/vrx_ws/install/local_setup.bash && ros2 launch vrx_gazebo generate_wamv.launch.py component_yaml:=/home/config/component_config.yaml thruster_yaml:=/home/config/thruster_config.yaml wamv_target:=/home/config/wamv_target.urdf wamv_locked:=False"]
ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/humble/setup.bash && source /home/vrx_ws/install/local_setup.bash && ros2 launch vrx_gz competition.launch.py world:=sydney_regatta headless:=true urdf:=/home/config/wamv_target.urdf"]