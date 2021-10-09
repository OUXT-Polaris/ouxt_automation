cd ansible
sh setup_ansible.sh
cd ../
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --vars ansible/vars/github_token.yaml --connection local --ask-become-pass --ask-vault-pass