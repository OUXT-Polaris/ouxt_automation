# Build Document

Documentation is robotx_setup is automatically deployed [here](https://ouxt-polaris.github.io/robotx_setup/).  
But if you want to build documentation manually, please check here.  

## only first time
```
sudo apt install ansible
```
install ansible in order to run playbook.  
mkdocs and other dependency was resolved by this playbook.  

## build document
```
cd (directory of robotx_setup)
ansible-playbook -i ansible/hosts/localhost.ini ansible/build_document.yml --connection local --ask-become-pass
cd docs
mkdocs serve
```