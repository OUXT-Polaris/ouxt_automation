sh install_poetry.sh
poetry install
poetry run ansible-playbook -i ansible/hosts/uav.ini ansible/setup_uav.yml --connection ssh --ask-become-pass
