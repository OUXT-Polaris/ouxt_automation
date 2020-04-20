# OUXT Polaris Environment Setup Tool ![robotx_setup](https://github.com/OUXT-Polaris/robotx_setup/workflows/robotx_setup/badge.svg)

## How to use

### Base Environments

```
Ubuntu 18.04
```

ansible task install ROS2 eloquent, so you do not necessary to setup ROS2

before you run makefile, you have to install ansible via apt

```
sudo apt install ansible
```

### install in local host (full package)

```
make local_setup_full
```