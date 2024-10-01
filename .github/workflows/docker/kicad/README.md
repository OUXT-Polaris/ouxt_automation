# Docker container for OUXT Polaris circuit development

## WHat is it?

This image is based on [this docker image](https://docs.linuxserver.io/images/docker-kicad/).
This image contains kicad library which is necessary for circuit development.
You do not need to install library manually.

## Software versions

KiCAD 8.0.1

## KiCAD Library

- [KiCad-RP-Pico](https://github.com/ncarandini/KiCad-RP-Pico)

## How to use

```bash
git clone https://github.com/OUXT-Polaris/ouxt_automation
cd ouxt_automation/circuits
sh start_kicad.sh
```

Open [http://localhost:3000/](http://localhost:3000/)

![kicad](https://raw.githubusercontent.com/OUXT-Polaris/ouxt_automation/refs/heads/master/.github/workflows/docker/kicad/kicad.png)
