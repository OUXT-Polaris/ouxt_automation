# Build Instractions

If you want to know about supported platfroms, please see also [this page](supported_platforms.md).

## setup develop environment (full package)

first time
```
sudo apt install ansible
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass
```

not first time
```
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass --skip-tags create_workspace --skip-tags setup_ros2
```

## setup develop container

```
cd docker/build_test
sh run.sh
cd ../
ansible-playbook -i ansible/hosts/docker.ini ansible/setup_dev_container.yml
```