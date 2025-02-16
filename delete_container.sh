#!/bin/bash

# Delete container
docker compose down

# Delete Enviroment Variable
sed -i '/export USER_ID=/d' ~/.bashrc
sed -i '/export GROUP_ID=/d' ~/.bashrc
sed -i '/export OUXT_AUTOMATION=/d' ~/.bashrc
export -n USER_ID
export -n GROUP_ID
export -n OUXT_AUTOMATION

# Delete alias
sed -i '/alias ros2_start=/d' ~/.bash_aliases
eval "$(cat ~/.bashrc | tail -n +10)"
