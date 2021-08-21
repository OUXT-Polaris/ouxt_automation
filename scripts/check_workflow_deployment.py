import argparse
import yaml
import subprocess
import sys

def check_workflow_deployment(repos_filepath, workflow_name):
    with open(repos_filepath) as file:
        repos_yaml = yaml.safe_load(file)
        for repository in repos_yaml['repositories']:
            command = ["gh", "workflow", "view", "-R", repos_yaml['repositories'][repository]['url'], workflow_name]
            print(command)
            code = subprocess.call(command)
            if code != 0:
                sys.exit(code)
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='python script for overwriting repos file')
    parser.add_argument('repos_filepath', help='path to the repos file')
    parser.add_argument('workflow_name', help='name of the workflow you want to exist')
    args = parser.parse_args()
    check_workflow_deployment(args.repos_filepath, args.workflow_name)