#!/bin/bash -l
cd /home/runner/actions-runner
curl -u wamvtan:$GITHUB_TOKEN -X POST -H "Accept: application/vnd.github.v3+json" https://api.github.com/repos/OUXT-Polaris/dataset_annotations/actions/runners/registration-token | jq '.token' | tr -d \" | { read v ;./config.sh --url https://github.com/OUXT-Polaris/dataset_annotations --token "$v" --labels yolox_trainer --ephemeral;}
./run.sh