local_setup_full:
	ansible-playbook -i ansible/hosts/hosts.ini ansible/setup_full.yml --connection local --become
