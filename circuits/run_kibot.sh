docker run --name=kicad \
  --rm \
  -v ${PWD}/computer_sensor_board:/workspace/computer_sensor_board \
  -v ${PWD}/3rdparty:/root/.local/share/kicad/8.0/3rdparty \
  wamvtan/kicad:latest kibot -c /workspace/kibot.yaml -e /workspace/computer_sensor_board/design/design.kicad_sch
