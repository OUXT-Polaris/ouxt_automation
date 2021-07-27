FROM ros:foxy

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS=yes

RUN sudo apt-get update && sudo apt-get -y install python3-pip python3-rospkg python3-rosdep
RUN mkdir -p /robotx_ws/src

WORKDIR /robotx_ws
COPY . /robotx_ws
RUN vcs import src < packages.repos
RUN source /opt/ros/foxy/setup.bash && rosdep install -iry --from-paths src --rosdistro foxy
RUN source /opt/ros/foxy/setup.bash && colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release