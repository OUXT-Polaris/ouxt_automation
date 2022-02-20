FROM dustynv/ros:galactic-ros-base-l4t-r32.5.0
ENV DEBIAN_FRONTEND=noninteractive
RUN mkdir -p ~/perception_camera_ws/src
WORKDIR ~/perception_camera_ws/src
ADD https://api.github.com/repos/OUXT-Polaris/image_processing_utils/git/refs/heads/master image_processing_utils_version.json
RUN git clone https://github.com/OUXT-Polaris/image_processing_utils.git
WORKDIR ~/perception_camera_ws/
RUN colcon build --symlink-install