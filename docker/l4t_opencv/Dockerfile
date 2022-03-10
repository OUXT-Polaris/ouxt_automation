FROM nvcr.io/nvidia/l4t-base:r32.5.0

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      cmake \
      file \
      gfortran \
      git \
      libatlas-base-dev \
      libavcodec-dev \
      libavcodec-dev \
      libavformat-dev \
      libavformat-dev \
      libavresample-dev \
      libavutil-dev \
      libcanberra-gtk3-module \
      libdc1394-22-dev \
      libeigen3-dev \
      libglew-dev \
      libgstreamer-plugins-base1.0-dev \
      libgstreamer-plugins-good1.0-dev \
      libgstreamer1.0-dev \
      libgtk-3-dev \
      libgtkglext1 \
      libgtkglext1-dev \
      libjpeg-dev \
      libjpeg-turbo8-dev \
      libjpeg8-dev \
      liblapack-dev \
      liblapacke-dev \
      libopenblas-dev \
      libpng-dev \
      libpostproc-dev \
      libswscale-dev \
      libswscale-dev \
      libtbb-dev \
      libtbb2 \
      libtesseract-dev \
      libtiff-dev \
      libv4l-dev \
      libx264-dev \
      libxine2-dev \
      libxvidcore-dev \
      pkg-config \
      qv4l2 \
      tar \
      v4l-utils \
      v4l2ucp \
      zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

ARG OPENCV_VERSION="4.5.0"

RUN git config --global http.sslVerify false && \
    git clone --depth 1 --branch $OPENCV_VERSION https://github.com/opencv/opencv.git && \
    git clone --depth 1 --branch $OPENCV_VERSION https://github.com/opencv/opencv_contrib.git

WORKDIR /opencv
RUN mkdir /opencv/build
WORKDIR /opencv/build

RUN cmake \
  -D BUILD_BUILD_JASPER=OFF \
  -D BUILD_DOCS=OFF \
  -D BUILD_EXAMPLES=OFF \
  -D BUILD_JPEG=ON \
  -D BUILD_opencv_apps=OFF \
  -D BUILD_opencv_cudev=OFF \
  -D BUILD_opencv_world=OFF \
  -D BUILD_opencv_python2=OFF \
  -D BUILD_opencv_python3=OFF \
  -D BUILD_PERF_TESTS=OFF \
  -D BUILD_PNG=ON \
  -D BUILD_TESTS=OFF \
  -D BUILD_TIFF=ON \
  -D BUILD_ZLIB=ON \
  -D CMAKE_BUILD_TYPE=RELEASE \
  -D EIGEN_INCLUDE_PATH=/usr/include/eigen3 \
  -D FORCE_VTK=OFF \
  -D opencv_cudev=OFF \
  -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
  -D WITH_CAROTENE=OFF \
  -D WITH_CUDA=OFF \
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
  -D OPENCV_ENABLE_NONFREE=ON \
../ && \
  make -j$(nproc) && \
  make install

WORKDIR /
RUN rm -rf opencv opencv_contrib