#!/bin/bash

# Check arguments
if [ $# != 1 ]; then
    echo "Requires a passward to be set in the argument"
    return 1
fi

# Set alias
path=$(pwd)
sudo chmod +x ./robotx_ws_docker.sh
alias robotx_ws_docker
if [[ $? != 0 ]]; then
    echo "alias robotx_ws_docker=$path/robotx_ws_docker.sh" >>~/.bash_aliases
fi

# Set Environment Variables (UID and GID)
echo "export USER_ID=$(id -u)" >>~/.bashrc
echo "export GROUP_ID=$(id -g)" >>~/.bashrc
echo "export OUXT_AUTOMATION=$path" >>~/.bashrc

# Reload bashrc
eval "$(cat ~/.bashrc | tail -n +10)"

#############################################################################
# Create and Start container
docker compose build $2
docker compose create
docker compose start

## Set passward
docker compose exec robotx_ws sh -c "echo "ros:$1" | chpasswd"

## Stop Container
docker compose stop
#############################################################################
