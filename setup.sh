sh install_poetry.sh
poetry install
poetry run ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass -e ansible_user=${USER}
