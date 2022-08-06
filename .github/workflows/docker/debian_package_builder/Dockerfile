ARG ROS_DISTRO=galactic
FROM ros:$ROS_DISTRO

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3-bloom \
      fakeroot \
      dpkg-dev \
      debhelper \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean