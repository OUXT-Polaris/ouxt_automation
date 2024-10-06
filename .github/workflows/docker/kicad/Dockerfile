FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    software-properties-common \
    wget \
    curl \
    && add-apt-repository --yes ppa:kicad/kicad-8.0-releases \
    && apt-get update && apt-get install -y \
    python3-pip \
    kicad \
    xvfb \
    x11-apps \
    && apt-get clean

RUN pip3 install kibot --no-compile

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
