local_setup_full:
	ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_full.yml --connection local --ask-sudo-pass