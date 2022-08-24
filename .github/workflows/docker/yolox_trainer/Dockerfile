FROM wamvtan/yolox

# set noninteractive
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS=yes

# arguments
ARG os
ARG runner_version
ARG github_token

# install curl
RUN apt-get update -y
RUN apt-get install curl jq -y

# pass github token
ENV GITHUB_TOKEN=${github_token}

# setup entry point
COPY entrypoint.sh /entrypoint.sh
RUN ["chmod", "+x", "/entrypoint.sh"]

# making runner user
ARG USERNAME=runner
ARG GROUPNAME=runner
ARG UID=1000
ARG GID=1000
RUN groupadd --gid $GID $USERNAME \
    && useradd --uid $UID --gid $GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# install cacched library
RUN apt-get update && apt-get install -y libboost-all-dev debconf-utils keyboard-configuration

USER $USERNAME
WORKDIR /home/$USERNAME/
# make directory for runner
RUN mkdir actions-runner
WORKDIR /home/$USERNAME/actions-runner
# untar runner
RUN curl -o actions-runner-${os}-${runner_version}.tar.gz -L https://github.com/actions/runner/releases/download/v${runner_version}/actions-runner-${os}-${runner_version}.tar.gz
RUN tar -xzf ./actions-runner-${os}-${runner_version}.tar.gz

ENTRYPOINT ["bash", "/entrypoint.sh"]