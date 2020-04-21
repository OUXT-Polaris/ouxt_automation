# OUXT Polaris Environment Setup Tool ![robotx_setup](https://github.com/OUXT-Polaris/robotx_setup/workflows/robotx_setup/badge.svg)

## How to use

### Base Environments

```
Ubuntu 18.04
```

ansible task install ROS2 eloquent, so you do not necessary to setup ROS2

before you run ansible-script, you have to install ansible via apt

```
sudo apt install ansible
```

### install in local host (full package)

```
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_full.yml --connection local --ask-sudo-pass
```

### install to test docker image

```
cd docker
sh run.sh
ansible-playbook -i ansible/hosts/docker.ini ansible/setup_full.yml
```