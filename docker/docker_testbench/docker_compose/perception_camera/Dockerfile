FROM nvcr.io/nvidia/l4t-ml:r32.5.0-py3
ENV DEBIAN_FRONTEND=noninteractive
#RUN curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--docker" sh -s -

RUN apt-get update
RUN apt-get install -y openssh-server locales
RUN mkdir /var/run/sshd
RUN echo 'jetson:jetson' | chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]