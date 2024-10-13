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
    unzip \
    git \
    && apt-get clean

RUN pip3 install kibot --no-compile

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /usr/share/kicad/footprints
RUN git clone https://github.com/XenGi/teensy.pretty.git

WORKDIR /usr/share/kicad/symbols
RUN git clone https://github.com/XenGi/teensy_library.git
RUN kicad-cli sym upgrade teensy_library/teensy.lib -o teensy.kicad_sym

# RUN mkdir -p ~/.config/kicad/8.0
COPY fp-lib-table /root/.config/kicad/8.0
COPY sym-lib-table /root/.config/kicad/8.0

WORKDIR /workspace

ENTRYPOINT ["/entrypoint.sh"]
