# ML Pipeline
## What we can do?
We can train / convert yolox model automatically.

## Install

```
ansible-galaxy install -fr ansible/roles/requirements.yml
ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_ml_pipeline.yml --connection local --ask-become-pass
```