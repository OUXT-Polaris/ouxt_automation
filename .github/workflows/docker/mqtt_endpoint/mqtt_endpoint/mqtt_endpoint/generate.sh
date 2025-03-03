protoc -I=$PWD/proto --python_out=. $PWD/proto/hardware_communication_msgs__HeartBeat.proto
protoc -I=$PWD/proto --python_out=. $PWD/proto/hardware_communication_msgs__MotorControl.proto

