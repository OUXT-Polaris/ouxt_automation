ARG BASE_IMAGE
FROM $BASE_IMAGE

RUN apt-get update && \
  apt-get install -y git python3 python3-pip && \
  apt-get -y clean && \
  rm -rf /var/lib/apt/lists/*
RUN pip3 install ansible\==2.9.8
WORKDIR /home
COPY tmp/ouxt_automation /home/ouxt_automation
WORKDIR /home/ouxt_automation
RUN ansible-playbook -i ansible/hosts/localhost.ini ansible/setup_dev_environment.yml --connection local --ask-become-pass -e ansible_user=root

WORKDIR /
ARG ENTRYPOINT_SH
COPY ${ENTRYPOINT_SH} /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
