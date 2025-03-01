ARG BASE_IMAGE=docker.io/hakuturu583/cuda_ros:lt4-humble-cuda-12.2.2-devel

FROM $BASE_IMAGE
SHELL ["/bin/bash", "-c"]

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y \
    python3-vcstool git python3-colcon-common-extensions python3-rosdep python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /wamv_ws/src
WORKDIR /wamv_ws/src
COPY ./repos/packages_exact.repos packages_exact.repos
RUN vcs import . < packages_exact.repos
WORKDIR ../
ENV USE_NCCL 0
ENV USE_DISTRIBUTED 1
ENV TORCH_CUDA_ARCH_LIST 8.7
RUN rosdep init && rosdep update

RUN --mount=type=cache,target=/wamv_ws/build source /opt/ros/$ROS_DISTRO/setup.bash && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    rosdep install -iry --from-paths src && \
    sudo apt-get install -y ros-$ROS_DISTRO-rmw-cyclonedds-cpp && \
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

RUN source /opt/ros/$ROS_DISTRO/setup.bash && \
    colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
