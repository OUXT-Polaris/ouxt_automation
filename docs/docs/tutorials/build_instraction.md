# Build Instractions

If you want to know about supported platfroms, please see also [this page](supported_platforms.md).

## setup develop environment (full package)

first time
```shell
sh setup.sh
```

not first time (skip installing ros2)
```shell
sh update.sh
```

## setup develop container

```
cd docker/build_test
sh run.sh
cd ../
ansible-playbook -i ansible/hosts/docker.ini ansible/setup_dev_container.yml
```