protoc -I=$PWD/proto --python_out=. $PWD/proto/hardware_communication_msgs__MotorControl.proto
protoc -I=$PWD/proto --python_out=. $PWD/proto/ground_station_heartbeat.proto
