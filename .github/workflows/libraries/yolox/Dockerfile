FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-devel
ENV DEBIAN_FRONTEND noninteractive
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-get update && \
  apt-get install -y git libgl1-mesa-dev libopencv-dev && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install nvidia-pyindex packaging && \
  python3 -m pip install --upgrade nvidia-tensorrt
WORKDIR /
RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt.git
WORKDIR /torch2trt
RUN python3 setup.py install --plugins
WORKDIR /
RUN git clone https://github.com/Megvii-BaseDetection/YOLOX.git
WORKDIR /YOLOX
RUN python3 -m pip install -r requirements.txt &&\
  python3 setup.py develop