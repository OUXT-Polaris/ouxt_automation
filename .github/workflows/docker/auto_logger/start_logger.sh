vcs export ../../../../robotx_ws/src/ --exact > packages_exact.repos
mkdir -p ${HOME}/auto_logger/rosbag
docker-compose up -d
