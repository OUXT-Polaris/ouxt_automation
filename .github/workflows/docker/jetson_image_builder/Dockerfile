FROM docker/compose:debian-1.29.2

# install qemu
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      qemu-user-static \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get clean

# download SD card image for jetson nano
RUN mkdir /jetpack_root
ADD https://developer.nvidia.com/embedded/l4t/r32_release_v7.1/jp_4.6.1_b110_sd_card/jeston_nano/jetson-nano-jp461-sd-card-image.zip /jetpack_root
ENV JETPACK_ROOT /jetpack_root

# copy docker-compose.yaml and entrypoint
ADD docker-compose.yaml /

# build jetson image
WORKDIR /
RUN docker-compose build