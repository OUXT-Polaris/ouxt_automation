sudo docker stop $(sudo docker ps -q)
sudo docker rmi $(sudo docker images -q) -f
sudo docker build -t ouxt-polaris .
sudo docker run -p 2022:22 -d ouxt-polaris