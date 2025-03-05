ARG ROS_DISTRO=humble
FROM ros:${ROS_DISTRO}-ros-core
SHELL ["/bin/bash", "-c"]

ARG UID=1000
ARG GID=1000

RUN groupadd -g $GID logger_user && \
    useradd -m -u $UID -g $GID logger_user

USER logger_user

RUN apt update && \
    apt install -y ros-$ROS_DISTRO-rosbag2-storage-mcap ros-$ROS_DISTRO-rosbag2 python3-vcstool python3-rosdep git python3-colcon-common-extensions && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p messages_ws/src

WORKDIR messages_ws
COPY packages_exact.repos packages_exact.repos
RUN vcs import src < packages_exact.repos

RUN rosdep init && \
    rosdep update && \
    apt update && \
    source /opt/ros/$ROS_DISTRO/setup.bash && \
    rosdep install -iry --from-paths $(colcon list -p | xargs -I{} bash -c 'if [ "`cat {}/package.xml | grep "rosidl_interface_packages"`" ]; then echo {}; fi') && \
    apt-get clean  && \
    rm -rf /var/lib/apt/lists/*

RUN source /opt/ros/$ROS_DISTRO/setup.bash && \
    colcon build --packages-select $(colcon list -n | xargs -I{} bash -c 'if [ "`cat {}/package.xml | grep "rosidl_interface_packages"`" ]; then echo {}; fi' | xargs)

ENV ROS_LOCALHOST_ONLY 0

RUN mkdir /rosbag

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
