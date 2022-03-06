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

WORKDIR /opt


#
# OpenCV - https://github.com/mdegans/nano_build_opencv/blob/master/build_opencv.sh
#

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        cmake \
        git \
        libavcodec-dev \
        libavformat-dev \
        libdc1394-22-dev \
        libgstreamer-plugins-base1.0-dev \
        libgstreamer1.0-dev \
        libgtk2.0-dev \
        libjpeg-dev \
        libpng-dev \
        libswscale-dev \
        libtbb2 libtbb-dev \
        libtiff-dev \
        libv4l-dev \
        pkg-config \
        python-dev \
        python-numpy \
        python2.7-dev \
        python3-numpy \
        python3.6-dev \
        qv4l2 \
        v4l-utils \
        v4l2ucp \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

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

ARG OPENCV_VERSION=4.5.0
RUN git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv.git
RUN git clone --depth 1 --branch ${OPENCV_VERSION} https://github.com/opencv/opencv_contrib.git

COPY ./build.sh /
RUN chmod a+x /build.sh
RUN mkdir build

ENTRYPOINT ["/build.sh"]