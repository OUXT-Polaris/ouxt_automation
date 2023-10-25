# dev_container

## How to use

### nogui
```bash
docker run -it --rm wamvtan/dev_container /bin/bash
```

### with vnc

```bash
docker run -p 6080:80 --shm-size=512m wamvtan/dev_container_vnc
```

open [http://127.0.0.1:6080/](http://127.0.0.1:6080/) on the browser.

## Recomended usage

Install vscode and devcontainers plugin.   
Official documetnation of this plugin is [here.](https://code.visualstudio.com/docs/remote/containers)    
