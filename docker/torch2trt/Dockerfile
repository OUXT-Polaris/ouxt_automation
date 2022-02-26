FROM nvcr.io/nvidia/pytorch:21.09-py3
RUN python3 -m pip install nvidia-pyindex packaging && \
  python3 -m pip install --upgrade nvidia-tensorrt
RUN apt-get update && \
  apt-get install -y git && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/*
WORKDIR /
RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt.git
WORKDIR /torch2trt
RUN python3 setup.py install --plugins
WORKDIR /
RUN git clone https://github.com/Megvii-BaseDetection/YOLOX.git
WORKDIR /YOLOX
RUN python3 -m pip install -r requirements.txt