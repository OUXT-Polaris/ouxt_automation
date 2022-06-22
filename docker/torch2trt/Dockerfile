FROM nvcr.io/nvidia/pytorch:21.09-py3
RUN python3 -m pip install nvidia-pyindex packaging && \
  python3 -m pip install nvidia-tensorrt==8.2.1.8
RUN apt-get update && \
  apt-get install -y git libgl1-mesa-dev && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/*
WORKDIR /
RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt.git
WORKDIR /torch2trt
RUN python3 setup.py install --plugins
WORKDIR /
RUN git clone https://github.com/Megvii-BaseDetection/YOLOX.git
WORKDIR /YOLOX
RUN python3 -m pip install -r requirements.txt &&\
  python3 setup.py develop
RUN mkdir model