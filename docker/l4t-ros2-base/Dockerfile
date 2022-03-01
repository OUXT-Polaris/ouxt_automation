FROM arm64v8/ros:galactic

ARG CUDA=10.2
ARG RELEASE="r32.6"
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt-get install -qq -y --no-install-recommends gnupg wget ca-certificates
RUN apt-key adv --fetch-key http://repo.download.nvidia.com/jetson/jetson-ota-public.asc && \
    echo "deb https://repo.download.nvidia.com/jetson/common $RELEASE main\ndeb https://repo.download.nvidia.com/jetson/t210 r32.6 main" >> \
    /etc/apt/sources.list.d/nvidia-l4t-apt-source.list && apt update && \
    CUDAPKG=$(echo $CUDA | sed 's/\./-/'); \
    apt install -y nvidia-cudnn8 \
    	cuda-libraries-$CUDAPKG \
	cuda-nvtx-$CUDAPKG \
	cuda-libraries-dev-$CUDAPKG \
	cuda-minimal-build-$CUDAPKG \
	cuda-license-$CUDAPKG \
	cuda-command-line-tools-$CUDAPKG \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/local/cuda-$CUDA /usr/local/cuda && \
    ln -s /usr/local/cuda-$CUDA/targets/aarch64-linux/include /usr/local/cuda/include && \
    ln -s /usr/local/cuda-$CUDA/targets/aarch64-linux/lib /usr/local/cuda/lib64

ENV PATH /usr/local/cuda-$CUDA/bin:/usr/local/cuda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/cuda-$CUDA/targets/aarch64-linux/lib:${LD_LIBRARY_PATH}

RUN ldconfig

ENV NVIDIA_VISIBLE_DEVICES all
ENV NVIDIA_DRIVER_CAPABILITIES all

##############################
### FIXME: NVIDIA's OpenCV ###
##############################
RUN wget \
  http://ports.ubuntu.com/pool/main/libv/libvpx/libvpx5_1.7.0-3ubuntu0.18.04.1_arm64.deb \
  http://ports.ubuntu.com/pool/universe/f/ffmpeg/libavcodec57_3.4.8-0ubuntu0.2_arm64.deb \
  http://ports.ubuntu.com/pool/universe/f/ffmpeg/libavformat57_3.4.8-0ubuntu0.2_arm64.deb \
  http://ports.ubuntu.com/pool/universe/f/ffmpeg/libavutil55_3.4.8-0ubuntu0.2_arm64.deb \
  http://ports.ubuntu.com/pool/universe/f/ffmpeg/libswresample2_3.4.8-0ubuntu0.2_arm64.deb \
  http://ports.ubuntu.com/pool/universe/f/ffmpeg/libswscale4_3.4.8-0ubuntu0.2_arm64.deb \
  http://ports.ubuntu.com/pool/universe/x/x264/libx264-152_0.152.2854+gite9a5903-2_arm64.deb \
  http://ports.ubuntu.com/pool/universe/x/x265/libx265-146_2.6-3_arm64.deb && \
  apt update && apt install -y \
  ./libvpx5_*_arm64.deb \
  ./libavcodec57_*_arm64.deb \
  ./libavformat57_*_arm64.deb \
  ./libavutil55_*_arm64.deb \
  ./libswresample2_*_arm64.deb \
  ./libswscale4_*_arm64.deb \
  ./libx264-152_*_arm64.deb \
  ./libx265-146_*_arm64.deb && \
  rm -rf /var/lib/apt/lists/* && apt clean


RUN apt update && \
  apt install -y --allow-downgrades --allow-change-held-packages \
  nvidia-opencv \
  libopencv \
  libopencv-dev=4.1.1-2-gd5a58aa75 \
  libopencv-python \
  libopencv-samples \
  opencv-licenses && \
  apt-mark hold libopencv-dev && \
  apt install -y \
  libnvvpi1 \
  vpi1-demos \
  vpi1-dev \
  vpi1-samples \
  python-vpi1

#########
###L4T###
#########

## If on the real SoC, comment this out. ##
RUN mkdir -p /opt/nvidia/l4t-packages/.nv-l4t-disable-boot-fw-update-in-preinstall ## Disable check in preinst

RUN wget http://ports.ubuntu.com/pool/main/libf/libffi/libffi6_3.2.1-8_arm64.deb && \
    apt install -y ./libffi6_*_arm64.deb && \
    apt install systemd -y &&  apt -o Dpkg::Options::="--force-overwrite" install -y nvidia-l4t-init
    
RUN apt install -y \
  nvidia-l4t-camera \
  nvidia-l4t-jetson-io \
  nvidia-l4t-jetson-multimedia-api \
  nvidia-l4t-multimedia \
  nvidia-l4t-tools \
  nvidia-l4t-multimedia-utils \
#  nvidia-container \
#  nvidia-container-csv-* \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && ldconfig

CMD ["/bin/bash"]

