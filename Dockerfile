ARG ubuntu_ver=22.04
ARG base_image=ubuntu:$ubuntu_ver

FROM $base_image

ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-c"]


##################
## Install variety
##################
RUN apt update && apt install -y iproute2 gnupg2 lsb-release vim ansible locate && \
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
RUN <<EOT
apt install sudo gosu
useradd -ms /bin/bash ros
echo "export USER=ros" >> /home/ros/.bashrc
EOT

WORKDIR /home/ros

COPY ./entrypoint.sh /usr/bin
RUN chmod +x /usr/bin/entrypoint.sh
ENTRYPOINT [ "/bin/bash", "-c", "/usr/bin/entrypoint.sh" ]
