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

#########
###L4T###
#########

## If on the real SoC, comment this out. ##
RUN mkdir -p /opt/nvidia/l4t-packages/.nv-l4t-disable-boot-fw-update-in-preinstall ## Disable check in preinst

RUN wget http://ports.ubuntu.com/pool/main/libf/libffi/libffi6_3.2.1-8_arm64.deb && \
    apt install -y ./libffi6_*_arm64.deb && \
    apt update && apt install systemd -y &&  apt -o Dpkg::Options::="--force-overwrite" install -y nvidia-l4t-init \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    
RUN apt update && apt install -y \
  nvidia-l4t-camera \
  nvidia-l4t-jetson-io \
  nvidia-l4t-jetson-multimedia-api \
  nvidia-l4t-multimedia \
  nvidia-l4t-tools \
  nvidia-l4t-multimedia-utils \
  g++-8 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && ldconfig && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 8 && \
    update-alternatives --config gcc && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 8 && \
    update-alternatives --config g++

CMD ["/bin/bash"]

