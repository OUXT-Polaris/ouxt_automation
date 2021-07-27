# sudo docker stop $(sudo docker ps -q)
# sudo docker rmi $(sudo docker images -q) -f
SCRIPT_DIR=$(cd $(dirname $0); pwd)
cd $SCRIPT_DIR/..
# docker-compose build
docker-compose up -d
