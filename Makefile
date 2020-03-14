local:
	ansible-playbook -i ansible/hosts/hosts.ini ansible/setup_core.yml --connection local --ask-sudo-pass