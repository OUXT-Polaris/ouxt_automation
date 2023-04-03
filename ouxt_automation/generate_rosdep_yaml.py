import argparse
import subprocess
import yaml
import os

def generate_yaml(workspace_path):
    output = subprocess.check_output(['sh', 'generate_base_yaml.sh', workspace_path])
    data = yaml.load(output)
    for package in data:
        data[package]['ubuntu'][0] = data[package]['ubuntu'][0].replace("_", "-")
    yaml_string = yaml.dump(data)
    f = open('rosdep.yaml', 'w')
    f.write(yaml_string)
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='python script for generating rosdep_yaml file from workspace')
    parser.add_argument('workspace_path', help='full path to the workspace')
    args = parser.parse_args()
    generate_yaml(args.workspace_path)