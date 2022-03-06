#!/bin/bash
# ln -s /usr/include/aarch64-linux-gnu/cudnn_version_v8.h /usr/include/aarch64-linux-gnu/cudnn_version.h

rm -rf build/*
cd build && \
cmake \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_opencv_python2=OFF \
    -D BUILD_opencv_python3=OFF \
    -D BUILD_opencv_world=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D BUILD_TESTS=OFF \
    -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D CPACK_BINARY_DEB=ON \
    -D CUDA_ARCH_BIN="5.3,6.2,7.2" \
    -D CUDA_ARCH_PTX="" \
    -D CUDNN_INCLUDE_DIR=/usr/include/aarch64-linux-gnu \
    -D OPENCV_EXTRA_MODULES_PATH=/home/ubuntu/opencv_contrib/modules \
    -D OPENCV_GENERATE_PKGCONFIG=ON \
    -D WITH_CUDA=ON \
    -D WITH_CUDNN=ON \
    -D WITH_GSTREAMER=ON \
    -D WITH_LIBV4L=ON \
    -D WITH_TBB=ON \
    -D WITH_V4L=OFF \
/home/ubuntu/opencv

# make -j$(nproc)
# make install
# make package
# tar -czvf OpenCV-$OPENCV_VERSION-aarch64.tar.gz *.deb
# mv *.deb /home/ubuntu/deb