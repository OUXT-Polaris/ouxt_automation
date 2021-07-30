FROM hakuturu583/robotx_scenario_test:master

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive
ENV DEBCONF_NOWARNINGS=yes

WORKDIR /robotx_ws
COPY packages.repos /robotx_ws
RUN rm -rf /robotx_ws/src
RUN vcs import src < packages.repos
RUN source /opt/ros/foxy/setup.bash && rosdep install -iry --from-paths src --rosdistro foxy
RUN source /opt/ros/foxy/setup.bash && colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release