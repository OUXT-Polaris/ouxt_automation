ARG ubuntu_ver=22.04
ARG base_image=ubuntu:$ubuntu_ver

FROM $base_image

ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-c"]


##################
## Install variety
##################
RUN apt update && apt install -y iproute2 gnupg2 lsb-releas vim ansible qlocate && \
  updatedb


####################################################
## Enable completion
## ref: https://penguin-coffeebreak.com/archives/242
####################################################
RUN apt install bash-completion && source /etc/bash_completion && \
	rm /etc/apt/apt.conf.d/docker-clean && apt update


##################
## Create new user
##################
RUN @"
apt install sudo gosu
useradd -ms /bin/bash ros
echo "export USER=ros" >> /home/ros/.bashrc
"@

WORKDIR /home/ros

