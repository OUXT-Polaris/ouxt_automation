#!/bin/bash
# ln -s /usr/include/aarch64-linux-gnu/cudnn_version_v8.h /usr/include/aarch64-linux-gnu/cudnn_version.h

rm -rf build/*
cd build && \
cmake \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_opencv_python2=ON \
    -D BUILD_opencv_python3=ON \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_TESTS=OFF \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D CUDA_ARCH_BIN="5.3,6.2,7.2" \
    -D CUDA_ARCH_PTX="" \
    -D OPENCV_EXTRA_MODULES_PATH=/home/ubuntu/opencv_contrib/modules \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D WITH_CUDA=ON \
    -D WITH_CUDNN=ON \
    -D WITH_GSTREAMER=ON \
    -D WITH_LIBV4L=ON \
/home/ubuntu/opencv




# -D CUDNN_INCLUDE_DIR=/usr/include/aarch64-linux-gnu \

# make -j$(nproc)
# make install
# make package
# tar -czvf OpenCV-$OPENCV_VERSION-aarch64.tar.gz *.deb
# mv *.deb /home/ubuntu/deb