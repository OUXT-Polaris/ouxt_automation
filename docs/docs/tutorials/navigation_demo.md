# Navigation Demo

[![](https://img.youtube.com/vi/nkrm7e8vdPg/maxresdefault.jpg)](https://www.youtube.com/watch?v=nkrm7e8vdPg)

## How to run demo
### build packages
Please see also, [this page](build_instraction.md).

### run simulator and planner

```
ros2 launch navi_sim with_planner.launch.py behavior_config_filepath:=config/loop_demo.yaml
```

### set goal
use 2d goal pose tool in rviz.  
![set goal](./images/set_goal.png)

then, the navigation starts.  
![navigation](./images/navigation.png)

### spawn obstacle
use clicked point tool in rviz
![spawn obstacle](./images/spawn_obstacle.png)

then, replan waypoints.  
![replan](./images/replan.png)