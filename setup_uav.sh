cd ansible
sh setup_ansible.sh
cd ../
ansible-galaxy install -fr ansible/roles/requirements.yml
ansible-playbook -i ansible/hosts/uav.ini ansible/setup_uav.yml --connection local --ask-become-pass