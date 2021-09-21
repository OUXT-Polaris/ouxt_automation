# Build Instractions

If you want to know about supported platfroms, please see also [this page](supported_platforms.md).

## build this documentation locally
```
ansible-playbook -i ansible/hosts/localhost.ini ansible/build_document.yml --connection local --ask-become-pass
```


## setup develop environment (full package)

first time
```
sudo apt install ansible
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass
```

not first time
```
ansible-playbook -i ansible/hosts/localhost.ini ansible/update_full.yml --connection local --ask-become-pass
```

## setup develop container

```
cd docker/build_test
sh run.sh
cd ../
ansible-playbook -i ansible/hosts/docker.ini ansible/setup_dev_container.yml
```