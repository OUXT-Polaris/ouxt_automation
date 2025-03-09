mkdir -p $HOME/auto_logger/rosbag
ros2 bag record -o $HOME/auto_logger/rosbag/$(date '+%Y-%m-%d-%H-%M-%S') -d 10 -s mcap --storage-config-file $HOME/auto_logger/storage_options.yaml /wamv/sensors/cameras/front_camera_sensor/image_raw/compressed /wamv/sensors/lidars/front_lidar_sensor/velodyne_points /protokink/gps /protolink/imu
