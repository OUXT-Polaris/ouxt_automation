docker run --name=kicad \
  -e DISPLAY=$DISPLAY \
  --net=host \
  --rm \
  -v ${PWD}/computer_sensor_board:/workspace/computer_sensor_board \
  -v ${PWD}/3rdparty:/root/.local/share/kicad/8.0/3rdparty \
  wamvtan/kicad:latest
