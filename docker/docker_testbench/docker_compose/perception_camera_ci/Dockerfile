FROM dustynv/ros:galactic-ros-base-l4t-r32.5.0
ENV DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"] 
ENV SHELL /bin/bash

RUN mkdir -p /root/perception_camera_ws/src
WORKDIR /root/perception_camera_ws/src

#ADD https://api.github.com/repos/OUXT-Polaris/ouxt_common/git/refs/heads/master ouxt_common_version.json
RUN git clone https://github.com/OUXT-Polaris/ouxt_common.git
#ADD https://api.github.com/repos/OUXT-Polaris/image_processing_utils/git/refs/heads/master image_processing_utils_version.json
RUN git clone https://github.com/OUXT-Polaris/image_processing_utils.git
#ADD https://api.github.com/repos/OUXT-Polaris/tensorrt_yolox/git/refs/heads/main tensorrt_yolox_version.json
RUN git clone https://github.com/OUXT-Polaris/tensorrt_yolox.git
#ADD https://api.github.com/repos/ament/ament_lint/git/refs/heads/galactic ament_lint_version.json
RUN git clone -b galactic https://github.com/ament/ament_lint.git
#ADD https://api.github.com/repos/tier4/cudnn_cmake_module/git/refs/heads/main cudnn_cmake_module_version.json
RUN git clone -b main https://github.com/tier4/cudnn_cmake_module.git
#ADD https://api.github.com/repos/tier4/tensorrt_cmake_module/git/refs/heads/main tensorrt_cmake_module_version.json
RUN git clone -b main https://github.com/tier4/tensorrt_cmake_module.git
#ADD https://api.github.com/repos/tier4/cuda_utils/git/refs/heads/main cuda_utils_version.json
RUN git clone -b main https://github.com/tier4/cuda_utils.git
#ADD https://api.github.com/repos/tier4/tensorrt_common/git/refs/heads/main tensorrt_common_version.json
RUN git clone -b main https://github.com/tier4/tensorrt_common.git
RUN git clone -b galactic https://github.com/ros2/tinyxml2_vendor.git

RUN source /opt/ros/galactic/install/setup.bash && \
  apt-get update && \
  apt-get install -y libssl-dev &&\
  rosdep install -y -r -i --from-paths /root/perception_camera_ws/src --ignore-src --rosdistro galactic \
    --skip-keys "libopencv-dev libopencv-contrib-dev libopencv-imgproc-dev python-opencv python3-opencv"

WORKDIR /root/perception_camera_ws/
#ENTRYPOINT ["/bin/bash", "-c", "source /opt/ros/galactic/install/setup.bash && colcon build --symlink-install --packages-up-to tensorrt_common"]
#ADD entrypoint.sh /
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT ["/entrypoint.sh"]