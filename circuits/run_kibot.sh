docker run --name=kibot \
  --rm \
  -v ${PWD}/computer_sensor_board:/workspace/computer_sensor_board \
  -v ${PWD}/3rdparty:/root/.local/share/kicad/8.0/3rdparty \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/schematics:/workspace/schematics \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/pcb:/workspace/pcb \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/render:/workspace/render \
  wamvtan/kicad:latest kibot -c /workspace/kibot.yaml -e /workspace/computer_sensor_board/computer_sensor_board/computer_sensor_board.kicad_sch
