#!/bin/bash

cmake \
  -D BUILD_BUILD_JASPER=OFF \
  -D BUILD_DOCS=OFF \
  -D BUILD_EXAMPLES=OFF \
  -D BUILD_JPEG=ON \
  -D BUILD_opencv_apps=OFF \
  -D BUILD_opencv_cudev=ON \
  -D BUILD_opencv_python2=OFF \
  -D BUILD_opencv_python3=OFF \
  -D BUILD_PERF_TESTS=OFF \
  -D BUILD_PNG=ON \
  -D BUILD_TESTS=OFF \
  -D BUILD_TIFF=ON \
  -D BUILD_ZLIB=ON \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D CMAKE_LIBRARY_PATH=/usr/local/cuda/targets/aarch64-linux/lib/stubs \
  -D CPACK_BINARY_DEB=ON \
  -D CUDA_ARCH_BIN='5.3 6.2 7.2' \
  -D CUDA_TOOLKIT_ROOT_DIR=/usr/local/cuda/targets/aarch64-linux \
  -D CUDNN_INCLUDE_DIR=/usr/include/aarch64-linux-gnu \
  -D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
  -D FORCE_VTK=OFF \
  -D opencv_cudev=ON \
  -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
  -D WITH_CAROTENE=OFF \
  -D WITH_CUDA=ON \
  -D WITH_FFMPEG=OFF \
  -D WITH_GDAL=OFF \
  -D WITH_IPP=OFF \
  -D WITH_ITT=OFF \
  -D WITH_JASPER=OFF \
  -D WITH_LAPACK=OFF \
  -D WITH_OPENCL=OFF \
  -D WITH_OPENCLAMDBLAS=OFF \
  -D WITH_OPENCLAMDFFT=OFF \
  -D WITH_OPENEXR=OFF \
  -D WITH_OPENGL=OFF \
  -D WITH_PNG=ON \
  -D WITH_QT=OFF \
  -D WITH_TBB=OFF \
  -D WITH_TIFF=ON \
  -D WITH_VA_INTEL=OFF \
  -D WITH_WEBP=OFF \
  -D WITH_XINE=OFF \
  ../

make -j$(nproc)
make install
# make package

