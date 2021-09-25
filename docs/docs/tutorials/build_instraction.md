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
ansible-playbook -i ansible/hosts/docker.ini ansible/start_dev_container.yml
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local
```

## setup real robot

<span style="color: red; ">_NOTE_</span> : setting up real robot is fully automated via github actions, so using this setup-robot playbook manually is not recommended.

These operations should be run in robot.  
1. setup endpoint
```
sh ansible/setup_ansible.sh
export PERSONAL_ACCESS_TOKEN=$(ACCESS_TOKEN_OF_WAM_V_TAN_BOT)
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_endpoint.yml --connection local --ask-become-pass
```

If your want to know personal access token, please read [this documentation](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).