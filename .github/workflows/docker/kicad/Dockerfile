FROM ubuntu:24.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    software-properties-common \
    wget \
    curl \
    && add-apt-repository --yes ppa:kicad/kicad-9.0-releases \
    && apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    kicad \
    xvfb \
    x11-apps \
    unzip \
    git \
    && apt-get clean

RUN cd root && python3 -m venv --system-site-packages .venv && \
    echo "source ~/.venv/bin/activate" >> ~/.bashrc && \
    /bin/bash -c "source ~/.venv/bin/activate && \
    python -m pip install lxml && \
    python -m pip install kibot --no-compile"

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /usr/share/kicad/footprints
RUN git clone https://github.com/XenGi/teensy.pretty.git

WORKDIR /usr/share/kicad/symbols
RUN git clone https://github.com/XenGi/teensy_library.git
RUN kicad-cli sym upgrade teensy_library/teensy.lib -o teensy.kicad_sym

# RUN mkdir -p ~/.config/kicad/8.0
COPY fp-lib-table /root/.config/kicad/9.0
COPY sym-lib-table /root/.config/kicad/9.0

WORKDIR /workspace

COPY kibot.yaml /workspace/kibot.yaml

ENTRYPOINT ["/entrypoint.sh"]
