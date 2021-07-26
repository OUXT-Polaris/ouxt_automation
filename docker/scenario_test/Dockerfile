FROM ros:foxy
RUN mkdir -p robotx_ws/src
WORKDIR robotx_ws
COPY packages.repos robotx_ws/src
RUN vcs import src < packages.repos
RUN rosdep install -y -r -i --from-paths src --ignore-src --rosdistro foxy
RUN colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release