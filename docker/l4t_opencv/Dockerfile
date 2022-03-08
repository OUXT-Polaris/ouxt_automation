# 
# This is a Dockerfile for building OpenCV debian packages
# with CUDA, cuDNN, GStreamer, ect enabled.  You can then take
# the output .deb packages and install them into other containers.
#
# See scripts/docker_build_opencv.sh to run it
#

ARG BASE_IMAGE=nvcr.io/nvidia/l4t-base:r32.5.0
FROM ${BASE_IMAGE}

#
# setup environment
#
ENV DEBIAN_FRONTEND=noninteractive
ENV CUDA_HOME="/usr/local/cuda"
ENV PATH="/usr/local/cuda/bin:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/cuda/lib64:${LD_LIBRARY_PATH}"

#
# OpenCV - https://github.com/mdegans/nano_build_opencv/blob/master/build_opencv.sh
#

ARG UID=1000
ARG GID=1000
ARG UNAME=ubuntu
ARG HOSTNAME=docker
ARG USERNAME=$UNAME
ARG HOME=/home/$USERNAME

RUN useradd -u $UID -m $USERNAME && \
        echo "$USERNAME:$USERNAME" | chpasswd && \
        usermod --shell /bin/bash $USERNAME && \
        usermod -aG sudo $USERNAME && \
        mkdir /etc/sudoers.d && \
        echo "$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/$USERNAME && \
        chmod 0440 /etc/sudoers.d/$USERNAME && \
        usermod  --uid $UID $USERNAME && \
        groupmod --gid $GID $USERNAME && \
        chown -R $USERNAME:$USERNAME $HOME && \
        chmod 666 /dev/null && \
        chmod 666 /dev/urandom

WORKDIR /home/$USERNAME

ARG OPENCV_VERSION="4.4.0"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      cmake \
      file \
      gfortran \
      git \
      libatlas-base-dev \
      libavcodec-dev \
      libavcodec-dev \
      libavformat-dev \
      libavformat-dev \
      libavresample-dev \
      libavutil-dev \
      libcanberra-gtk3-module \
      libdc1394-22-dev \
      libeigen3-dev \
      libglew-dev \
      libgstreamer-plugins-base1.0-dev \
      libgstreamer-plugins-good1.0-dev \
      libgstreamer1.0-dev \
      libgtk-3-dev \
      libgtkglext1 \
      libgtkglext1-dev \
      libjpeg-dev \
      libjpeg-turbo8-dev \
      libjpeg8-dev \
      liblapack-dev \
      liblapacke-dev \
      libopenblas-dev \
      libpng-dev \
      libpostproc-dev \
      libswscale-dev \
      libswscale-dev \
      libtbb-dev \
      libtbb2 \
      libtesseract-dev \
      libtiff-dev \
      libv4l-dev \
      libx264-dev \
      libxine2-dev \
      libxvidcore-dev \
      pkg-config \
      qv4l2 \
      tar \
      v4l-utils \
      v4l2ucp \
      zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

RUN git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv.git && \
    git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv_contrib.git

WORKDIR /home/$USERNAME/opencv
RUN mkdir build

WORKDIR /home/$USERNAME/opencv/build

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/bin/sh", "-c", "/entrypoint.sh"]