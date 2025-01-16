docker run --name=kibot \
  --rm \
  -v ${PWD}/computer_sensor_board:/workspace/computer_sensor_board \
  -v ${PWD}/3rdparty:/root/.local/share/kicad/8.0/3rdparty \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/schematics:/workspace/schematics \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/pcb:/workspace/pcb \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/render:/workspace/render \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/gerber:/workspace/gerber \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/drill:/workspace/drill \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/bom:/workspace/bom \
  -v ${PWD}/../docs/docs/circuit/computer_sensor_board/kibot_output/zip:/workspace/zip \
  wamvtan/kicad:latest kibot -c /workspace/kibot.yaml -e /workspace/computer_sensor_board/computer_sensor_board/computer_sensor_board.kicad_sch

docker run --name=kibot \
  --rm \
  -v ${PWD}/miniv_motor_controller_board:/workspace/miniv_motor_controller_board \
  -v ${PWD}/3rdparty:/root/.local/share/kicad/8.0/3rdparty \
  -v ${PWD}/../docs/docs/circuit/miniv_motor_controller_board/kibot_output/schematics:/workspace/schematics \
  -v ${PWD}/../docs/docs/circuit/miniv_motor_controller_board/kibot_output/pcb:/workspace/pcb \
  -v ${PWD}/../docs/docs/circuit/miniv_motor_controller_board/kibot_output/render:/workspace/render \
  -v ${PWD}/../docs/docs/circuit/miniv_motor_controller_board/kibot_output/gerber:/workspace/gerber \
  -v ${PWD}/../docs/docs/circuit/miniv_motor_controller_board/kibot_output/drill:/workspace/drill \
  -v ${PWD}/../docs/docs/circuit/miniv_motor_controller_board/kibot_output/bom:/workspace/bom \
  -v ${PWD}/../docs/docs/circuit/miniv_motor_controller_board/kibot_output/zip:/workspace/zip \
  wamvtan/kicad:latest kibot -c /workspace/kibot.yaml -e /workspace/miniv_motor_controller_board/miniv_motor_controller_board/miniv_motor_controller_board.kicad_sch

docker run --name=kibot \
  --rm \
  -v ${PWD}/miniv_estop_board:/workspace/miniv_estop_board \
  -v ${PWD}/3rdparty:/root/.local/share/kicad/8.0/3rdparty \
  -v ${PWD}/../docs/docs/circuit/miniv_estop_board/kibot_output/schematics:/workspace/schematics \
  -v ${PWD}/../docs/docs/circuit/miniv_estop_board/kibot_output/pcb:/workspace/pcb \
  -v ${PWD}/../docs/docs/circuit/miniv_estop_board/kibot_output/render:/workspace/render \
  -v ${PWD}/../docs/docs/circuit/miniv_estop_board/kibot_output/gerber:/workspace/gerber \
  -v ${PWD}/../docs/docs/circuit/miniv_estop_board/kibot_output/drill:/workspace/drill \
  -v ${PWD}/../docs/docs/circuit/miniv_estop_board/kibot_output/bom:/workspace/bom \
  -v ${PWD}/../docs/docs/circuit/miniv_estop_board/kibot_output/zip:/workspace/zip \
  wamvtan/kicad:latest kibot -c /workspace/kibot.yaml -e /workspace/miniv_estop_board/miniv_estop_board/miniv_estop_board.kicad_sch
