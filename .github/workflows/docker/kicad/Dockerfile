FROM linuxserver/kicad:8.0.1

ENV KICAD8_3DMODEL_DIR="/usr/share/kicad/3dmodels/"
ENV KICAD8_FOOTPRINT_DIR="/usr/share/kicad/footprints/"
ENV KICAD8_SYMBOL_DIR="/usr/share/kicad/symbols/"

RUN mkdir kicad_libraries
WORKDIR /kicad_libraries
ADD https://github.com/ncarandini/KiCad-RP-Pico/archive/refs/heads/main.zip KiCad-RP-Pico.zip
RUN unzip KiCad-RP-Pico.zip

RUN cp -r "/kicad_libraries/KiCad-RP-Pico-main/RP-Pico Libraries/Pico.wrl" ${KICAD8_3DMODEL_DIR}
RUN cp -r "/kicad_libraries/KiCad-RP-Pico-main/RP-Pico Libraries/MCU_RaspberryPi_and_Boards.pretty" ${KICAD8_FOOTPRINT_DIR}
RUN cp -r "/kicad_libraries/KiCad-RP-Pico-main/RP-Pico Libraries/MCU_RaspberryPi_and_Boards.kicad_sym" ${KICAD8_SYMBOL_DIR}

WORKDIR /

COPY autostart /defaults/autostart
