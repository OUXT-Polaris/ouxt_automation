# OUXT Polaris Environment Setup Tool 

![robotx_setup](https://github.com/OUXT-Polaris/robotx_setup/workflows/robotx_setup/badge.svg)

![Documentation](https://github.com/OUXT-Polaris/robotx_setup/workflows/Documentation/badge.svg)

## How to use

### Base Environments

```
Ubuntu 20.04
```
If your ubuntu version is older than 20.04, you can use docker environment.  

ansible task install ROS2 foxy, so you do not necessary to setup ROS2

before you run ansible-script, you have to install ansible via apt

```
sudo apt install ansible
```

### build this documentation locally
```
ansible-playbook -i ansible/hosts/localhost.ini ansible/build_document.yml --connection local --ask-become-pass
```


### install in local host (full package)

first time
```
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_full.yml --connection local --ask-become-pass
```

not first time
```
ansible-playbook -i ansible/hosts/localhost.ini ansible/update_full.yml --connection local --ask-become-pass
```

### install to test docker image

```
cd docker
sh run.sh
ansible-playbook -i ansible/hosts/docker.ini ansible/setup_docker.yml
```
