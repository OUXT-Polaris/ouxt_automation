xhost +local:

docker run --name=kicad \
  -it \
  -e DISPLAY=$DISPLAY \
  --net=host \
  --rm \
  -v ${PWD}/computer_sensor_board:/workspace/computer_sensor_board \
  -v ${PWD}/miniv_motor_controller_board:/workspace/miniv_motor_controller_board \
  -v ${PWD}/miniv_estop_board:/workspace/miniv_estop_board \
  -v ${PWD}/smart_battery:/workspace/smart_battery \
  -v ${PWD}/3rdparty:/root/.local/share/kicad/8.0/3rdparty \
  wamvtan/kicad:latest kicad
