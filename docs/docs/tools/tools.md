# Tools

## Convert yolox pytorch model into tensorrt model.
### Requirement
- docker
- docker-compose
- nvidia-docker
- nvidia-gpu (hardware)

```
cd docker/torch2trt
sh convert.sh
```

Output should be like below.
```
docker-compose build

Building torch2trt
Step 1/12 : FROM nvcr.io/nvidia/pytorch:21.09-py3
 ---> 74d53f84c686
Step 2/12 : RUN python3 -m pip install nvidia-pyindex packaging &&   python3 -m pip install --upgrade nvidia-tensorrt
 ---> Using cache
 ---> 8d655c414dd2
Step 3/12 : RUN apt-get update &&   apt-get install -y git libgl1-mesa-dev &&   apt-get -y clean &&   rm -rf /var/lib/apt/lists/*
 ---> Using cache
 ---> 76bc393f04d5
Step 4/12 : WORKDIR /
 ---> Using cache
 ---> 47b28fa00606
Step 5/12 : RUN git clone https://github.com/NVIDIA-AI-IOT/torch2trt.git
 ---> Using cache
 ---> 1a4063050362
Step 6/12 : WORKDIR /torch2trt
 ---> Using cache
 ---> 6e679ba630a9
Step 7/12 : RUN python3 setup.py install --plugins
 ---> Using cache
 ---> f0f7dc347d9d
Step 8/12 : WORKDIR /
 ---> Using cache
 ---> 1d4ffaaae9a0
Step 9/12 : RUN git clone https://github.com/Megvii-BaseDetection/YOLOX.git
 ---> Using cache
 ---> 6cc15f5a7b36
Step 10/12 : WORKDIR /YOLOX
 ---> Using cache
 ---> 3429678d2547
Step 11/12 : RUN python3 -m pip install -r requirements.txt &&  python3 setup.py develop
 ---> Using cache
 ---> 377ef892e986
Step 12/12 : RUN mkdir model
 ---> Using cache
 ---> 55caa4a2787d
Successfully built 55caa4a2787d
Successfully tagged torch2trt_torch2trt:latest

docker-compose up

Recreating torch2trt_torch2trt_1 ... done
Attaching to torch2trt_torch2trt_1
torch2trt_1  | 
torch2trt_1  | =============
torch2trt_1  | == PyTorch ==
torch2trt_1  | =============
torch2trt_1  | 
torch2trt_1  | NVIDIA Release 21.09 (build 26760254)
torch2trt_1  | PyTorch Version 1.10.0a0+3fd9dcf
torch2trt_1  | 
torch2trt_1  | Container image Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
torch2trt_1  | 
torch2trt_1  | Copyright (c) 2014-2021 Facebook Inc.
torch2trt_1  | Copyright (c) 2011-2014 Idiap Research Institute (Ronan Collobert)
torch2trt_1  | Copyright (c) 2012-2014 Deepmind Technologies    (Koray Kavukcuoglu)
torch2trt_1  | Copyright (c) 2011-2012 NEC Laboratories America (Koray Kavukcuoglu)
torch2trt_1  | Copyright (c) 2011-2013 NYU                      (Clement Farabet)
torch2trt_1  | Copyright (c) 2006-2010 NEC Laboratories America (Ronan Collobert, Leon Bottou, Iain Melvin, Jason Weston)
torch2trt_1  | Copyright (c) 2006      Idiap Research Institute (Samy Bengio)
torch2trt_1  | Copyright (c) 2001-2004 Idiap Research Institute (Ronan Collobert, Samy Bengio, Johnny Mariethoz)
torch2trt_1  | Copyright (c) 2015      Google Inc.
torch2trt_1  | Copyright (c) 2015      Yangqing Jia
torch2trt_1  | Copyright (c) 2013-2016 The Caffe contributors
torch2trt_1  | All rights reserved.
torch2trt_1  | 
torch2trt_1  | NVIDIA Deep Learning Profiler (dlprof) Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
torch2trt_1  | 
torch2trt_1  | Various files include modifications (c) NVIDIA CORPORATION.  All rights reserved.
torch2trt_1  | 
torch2trt_1  | This container image and its contents are governed by the NVIDIA Deep Learning Container License.
torch2trt_1  | By pulling and using the container, you accept the terms and conditions of this license:
torch2trt_1  | https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license
torch2trt_1  | 
torch2trt_1  | NOTE: MOFED driver for multi-node communication was not detected.
torch2trt_1  |       Multi-node communication performance may be reduced.
torch2trt_1  | 
torch2trt_1  | NOTE: The SHMEM allocation limit is set to the default of 64MB.  This may be
torch2trt_1  |    insufficient for PyTorch.  NVIDIA recommends the use of the following flags:
torch2trt_1  |    nvidia-docker run --ipc=host ...
torch2trt_1  | 
torch2trt_1  | 2022-02-26 09:33:11.827 | INFO     | __main__:main:57 - loaded checkpoint done.
torch2trt_1  | [02/26/2022-09:33:13] [TRT] [I] [MemUsageChange] Init CUDA: CPU +188, GPU +0, now: CPU 1383, GPU 2123 (MiB)
torch2trt_1  | [02/26/2022-09:33:13] [TRT] [I] [MemUsageSnapshot] Begin constructing builder kernel library: CPU 1403 MiB, GPU 2123 MiB
torch2trt_1  | [02/26/2022-09:33:13] [TRT] [I] [MemUsageSnapshot] End constructing builder kernel library: CPU 1410 MiB, GPU 2123 MiB
torch2trt_1  | [02/26/2022-09:33:14] [TRT] [W] Tensor DataType is determined at build time for tensors not marked as input or output.
torch2trt_1  | [02/26/2022-09:33:14] [TRT] [W] FP16 support requested on hardware without native FP16 support, performance will be negatively affected.
torch2trt_1  | [02/26/2022-09:33:15] [TRT] [I] [MemUsageChange] Init cuBLAS/cuBLASLt: CPU +0, GPU +8, now: CPU 2107, GPU 2409 (MiB)
torch2trt_1  | [02/26/2022-09:33:15] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +8, now: CPU 2107, GPU 2417 (MiB)
torch2trt_1  | [02/26/2022-09:33:15] [TRT] [I] Local timing cache in use. Profiling results in this builder pass will not be stored.
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] Detected 1 inputs and 1 output network tensors.
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] Total Host Persistent Memory: 208144
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] Total Device Persistent Memory: 640512
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] Total Scratch Memory: 512
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] [MemUsageStats] Peak memory usage of TRT CPU/GPU memory allocators: CPU 4 MiB, GPU 294 MiB
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] [BlockAssignment] Algorithm ShiftNTopDown took 43.9912ms to assign 7 blocks to 214 nodes requiring 7181828 bytes.
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] Total Activation Memory: 7181828
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +10, now: CPU 2129, GPU 2477 (MiB)
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in building engine: CPU +3, GPU +4, now: CPU 3, GPU 4 (MiB)
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] [MemUsageChange] Init cuDNN: CPU +0, GPU +8, now: CPU 2128, GPU 2461 (MiB)
torch2trt_1  | [02/26/2022-09:33:48] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in IExecutionContext creation: CPU +0, GPU +8, now: CPU 3, GPU 12 (MiB)
torch2trt_1  | 2022-02-26 09:33:48.565 | INFO     | __main__:main:71 - Converted TensorRT model done.
torch2trt_1  | 2022-02-26 09:33:48.581 | INFO     | __main__:main:79 - Converted TensorRT model engine file is saved for C++ inference.
torch2trt_torch2trt_1 exited with code 0
```

### Build Jetson Nano Image 

