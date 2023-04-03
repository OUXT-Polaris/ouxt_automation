import argparse
import yaml
import subprocess
import sys

# Our repos which don't have actions named BuildTest or Release
# Specify Actions by {repository_name_in_rosdep_yaml}:{name_of_actions}
ignore_list = ["description/wamv_description:BuildTest", "description/wamv_description:Release"]

def check_workflow_deployment(repos_filepath, workflow_name):
    with open(repos_filepath) as file:
        repos_yaml = yaml.safe_load(file)
        for repository in repos_yaml['repositories']:
            url = repos_yaml['repositories'][repository]['url']
            if 'OUXT-Polaris' in url and f"{repository}:{workflow_name}" in ignore_list :
                print(f"❗ `{workflow_name}` in {repository} is marked ignored, so it's skipped.")
            elif 'OUXT-Polaris' in url:
                command = ["gh", "workflow", "view", "-R", url, workflow_name]
                print(command)
                code = subprocess.call(command)
                if code != 0:
                    sys.exit(code)
            else:
                print(f"❗  {url} is skipped because its origin is not us.")
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='python script for overwriting repos file')
    parser.add_argument('repos_filepath', help='path to the repos file')
    parser.add_argument('workflow_name', help='name of the workflow you want to exist')
    args = parser.parse_args()
    check_workflow_deployment(args.repos_filepath, args.workflow_name)
