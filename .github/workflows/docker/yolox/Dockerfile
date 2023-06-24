FROM nvidia/cuda:11.4.0-cudnn8-devel-ubuntu20.04
ENV DEBIAN_FRONTEND noninteractive
#RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-get update && \
  apt-get install -y git libgl1-mesa-dev libopencv-dev python3 python3-pip wget unzip && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/*
#RUN python3 -m pip install nvidia-pyindex packaging && \
#  python3 -m pip install nvidia-tensorrt==8.2.1.8 && \
RUN  python3 -m pip install cython && \
  python3 -m pip install opencv-python==4.5.5.64 && \
  python3 -m pip install 'git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI' && \
  python3 -m pip install tensorboard && \
  python3 -m pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113
WORKDIR /
#RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt.git
#WORKDIR /torch2trt
#RUN python3 setup.py install --plugins
WORKDIR /
RUN git clone https://github.com/Megvii-BaseDetection/YOLOX.git
WORKDIR /YOLOX
COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt &&\
  python3 setup.py develop
ENV PATH="${PATH}:/opt/hpcx/ompi/bin"
ENV LD_LIBRARY_PATH="${LD_LIBRARY_PATH}:/opt/hpcx/ompi/lib"
RUN mkdir model