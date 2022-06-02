FROM nvcr.io/nvidia/pytorch:21.09-py3
WORKDIR /
ADD https://api.github.com/repos/Megvii-BaseDetection/YOLOX/git/refs/heads/main version.json
RUN git clone https://github.com/Megvii-BaseDetection/YOLOX.git
WORKDIR /YOLOX
RUN python3 -m pip install -r requirements.txt &&\
  python3 setup.py develop