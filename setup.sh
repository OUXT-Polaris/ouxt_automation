cd ansible
sh setup_ansible.sh
cd ../
ansible-galaxy install -fr roles/requirements.yml
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass