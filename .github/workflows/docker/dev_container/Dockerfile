ARG BASE_IMAGE
FROM BASE_IMAGE

RUN apt-get update && \
  apt-get install -y git python3 python3-pip && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/*
RUN pip3 install ansible\==2.9.8

WORKDIR /home
ADD https://api.github.com/repos/OUXT-Polaris/ouxt_automation/git/refs/heads/master version.json
RUN git clone https://github.com/OUXT-Polaris/ouxt_automation.git

WORKDIR /home/ouxt_automation
RUN ansible-galaxy install -fr ansible/roles/requirements.yml
RUN ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass -e ansible_user=root
ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
