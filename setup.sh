cd ansible
sh setup_ansible.sh
cd ../
ansible-galaxy install -fr ansible/roles/requirements.yml
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass -e ansible_user=${USER}
