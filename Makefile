local:
	ansible-playbook -i ansible/hosts/hosts.ini ansible/setup_full.yml --connection local --ask-sudo-pass