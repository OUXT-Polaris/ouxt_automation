cd ansible
sh setup_ansible.sh
cd ../
ansible-playbook -i ansible/hosts/uav.ini ansible/setup_uav.yml --connection ssh --ask-become-pass