# Automation Pipeline

## Repository Architecture
OUXT-Polaris softwares are separeated in many repositories in order to run continuous integration quickly.  
So, we developing integration pipeline for operating complex software stacks and deploy it.

## Integration Pipeline

Integration pipeline is deployed at github actions in each repositories.

### Actions in robotx_setup package

You can see acions tatus [here](https://github.com/OUXT-Polaris/robotx_setup/actions).

#### robotx_setup
[![robotx_setup](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/ansible.yaml/badge.svg)](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/ansible.yaml)

```mermaid
graph TB
    pull_request --send -->robotx_setup
    developer --manual hook-->robotx_setup
    daily_hook --> robotx_setup

    linkStyle 0 stroke-width:2px,stroke:blue;
    linkStyle 1 stroke-width:2px,stroke:blue;
    linkStyle 2 stroke-width:2px,stroke:blue;

    click robotx_setup "https://github.com/OUXT-Polaris/robotx_setup" "robotx_setup repository"
```

robotx_setup job runs ansible with setup-full playbook and check the setup tool works well. 

```mermaid
graph TB
    pull_request --send -->robotx_setup
    developer --manual hook-->robotx_setup
    daily_hook --> robotx_setup

    linkStyle 0 stroke-width:2px,stroke:blue;
    linkStyle 1 stroke-width:2px,stroke:blue;
    linkStyle 2 stroke-width:2px,stroke:blue;

    click robotx_setup "https://github.com/OUXT-Polaris/robotx_setup" "robotx_setup repository"
```

build_docker job runs ansible with setup-docker playbook and check the setup tool works well with docker.

#### document
[![document](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/document.yaml/badge.svg)](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/document.yaml)

```mermaid
graph TB
    pull_request --send -->robotx_setup
    developer --manual hook-->robotx_setup
    daily_hook --> robotx_setup
    pull_request -- merged -->robotx_setup
    robotx_setup -- deploy --> github_pages

    linkStyle 0 stroke-width:2px,stroke:blue;
    linkStyle 1 stroke-width:2px,stroke:red;
    linkStyle 2 stroke-width:2px,stroke:red;
    linkStyle 3 stroke-width:2px,stroke:red;
    linkStyle 4 stroke-width:2px,stroke:red;

    click robotx_setup "https://github.com/OUXT-Polaris/robotx_setup" "robotx_setup repository"
    click github_pages "https://ouxt-polaris.github.io/robotx_setup/" "github pages"
```

documentation workflow generate this documentation site and deploy it into github pages.

#### deploy_workflow
[![deploy_workflow](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/deploy_workflow.yaml/badge.svg)](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/deploy_workflow.yaml)

```mermaid
graph TB
    developer --manual hook-->robotx_setup
    daily_hook --> robotx_setup
    robotx_setup -- deploy workflow --> target_repository

    linkStyle 0 stroke-width:2px,stroke:blue;
    linkStyle 1 stroke-width:2px,stroke:blue;
    linkStyle 2 stroke-width:2px,stroke:blue;

    click robotx_setup "https://github.com/OUXT-Polaris/robotx_setup" "robotx_setup repository"
```

deploy_workflow helps maintainers to deploy and maintain workflows for each pacakges.
currently, over 25 packages are maintained by this workflow.

#### check_workflow_deployment
[![check_workflow_deployment](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/check_workflow.yaml/badge.svg)](https://github.com/OUXT-Polaris/robotx_setup/actions/workflows/check_workflow.yaml)

```mermaid
graph TB
    developer --manual hook-->robotx_setup
    daily_hook --> robotx_setup
    robotx_setup -- check workflow exists --> target_repository
    robotx_setup -- if workflow does not exist --> slack
    robotx_setup -- request repos file --> artifact
    artifact -- send repos file --> robotx_setup

    linkStyle 0 stroke-width:2px,stroke:blue;
    linkStyle 1 stroke-width:2px,stroke:blue;
    linkStyle 2 stroke-width:2px,stroke:blue;
    linkStyle 3 stroke-width:2px,stroke:blue;
    linkStyle 4 stroke-width:2px,stroke:blue;
    linkStyle 5 stroke-width:2px,stroke:blue;

    click robotx_setup "https://github.com/OUXT-Polaris/robotx_setup" "robotx_setup repository"
```

check_workflow_deployment workflow checks github repositories in downloaded repos file and if the requred workflow does not exist in the target repository, notify this infomation to the team slack.

### Actions in each repositories

In each repository, pull requests automatically runs build tests, unit tests and scenario test.