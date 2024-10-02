docker run \
  --rm \
  --name=kicad \
  --security-opt seccomp=unconfined `#optional` \
  -e PUID=1000 \
  -e PGID=1000 \
  -e TZ=Etc/UTC \
  -p 3000:3000 \
  -p 3001:3001 \
  -v ${PWD}/computer_sensor_board:/config/circuits/computer_sensor_board \
  wamvtan/kicad:latest
