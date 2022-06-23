FROM docker/compose:1.29.2

# download SD card image for jetson nano
RUN mkdir /jetpack_root
ADD https://developer.nvidia.com/embedded/l4t/r32_release_v7.1/jp_4.6.1_b110_sd_card/jeston_nano/jetson-nano-jp461-sd-card-image.zip /jetpack_root
ENV JETPACK_ROOT /jetpack_root

# copy docker-compose.yaml and entrypoint
ADD docker-compose.yaml /
ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

# build jetson image
RUN docker-compose build
ENTRYPOINT ["/entrypoint.sh"]