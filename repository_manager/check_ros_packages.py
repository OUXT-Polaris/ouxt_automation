import argparse
from github import Github
import yaml
import git
import os
import shutil
from termcolor import colored

def check_ros_packages(token, yaml_path, send_pr):
    print(colored('start checking ROS2 packages', 'green'))
    workflow_dict = {"foxy" : "ROS2-Foxy.yaml", "dashing" : "ROS2-Dashing.yaml", "galactic" : "ROS2-Galactic.yaml"}
    g = Github(token)
    with open(yaml_path) as file:
        config = yaml.safe_load(file)
        for user in config["ros"]:
            i = 0
            for package in config["ros"][user]:
                url = "https://github.com/" + user + "/" + package + ".git"
                print("scanning -> " + url + "(" + str(i) + "/" + str(len(config["ros"][user])) + ")")
                support_platforms = []
                repo = g.get_repo(user + "/" + package)
                if config["ros"][user][package] is None:
                    support_platforms = list(workflow_dict.keys())
                elif "rosdistro" not in config["ros"][user][package]:
                    support_platforms = list(workflow_dict.keys())
                else:
                    support_platforms = config["ros"][user][package]["rosdistro"]
                branches = []
                for branch in repo.get_branches():
                    branches.append(branch.name)
                for platfrom in support_platforms:
                    commit_target = "workflow/" + platfrom
                    if commit_target not in branches:
                        check_ci_template(package, platfrom, user, repo, token, commit_target, send_pr)
                    else:
                        print(colored('branch ' + commit_target +  ' already exists, pass cheking CI template', 'yellow'))
                i = i + 1

def check_ci_template(package, rosdistro, user, repo, token, branch, send_pr):
    repo_path = os.path.join('./', 'ros_packages/' + package)
    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)
    clone_url = "https://" + user + ":" + token + "@github.com/" + user + "/" + package
    git_repo = git.Repo.clone_from(clone_url, repo_path, branch=repo.default_branch)
    git_repo.config_writer().set_value("user", "name", "robotx_buildfarm").release()
    git_repo.config_writer().set_value("user", "email", repo.organization.email).release()
    git_repo.git.branch(branch)
    git_repo.git.checkout(branch)
    workflow_dict = {"foxy" : "ROS2-Foxy.yaml", "dashing" : "ROS2-Dashing.yaml", "galactic" : "ROS2-Galactic.yaml"}
    if rosdistro not in workflow_dict:
        raise Exception("rosdistro key is invalid")
    else:
        with open("./ci_templates/" + workflow_dict[rosdistro], mode='r') as f:
            workflow_string_valid = f.read()
        workflow_string_valid = workflow_string_valid.replace("${package_name}", package)
        modified_files = []
        if not os.path.exists(repo_path + "/dependency.repos"):
            shutil.copyfile("./ci_templates/dependency.repos", repo_path + "/dependency.repos")
            modified_files.append(repo_path + "/dependency.repos")
        if os.path.exists(repo_path + "/.github/workflows/" + workflow_dict[rosdistro]):
            with open(repo_path + "/.github/workflows/" + workflow_dict[rosdistro], mode='r+') as f:
                workflow_string = f.read()
                if workflow_string != workflow_string_valid:
                    os.remove(repo_path + "/.github/workflows/" + workflow_dict[rosdistro])
                    with open(repo_path + "/.github/workflows/" + workflow_dict[rosdistro], mode='w') as workflow_file:
                        workflow_file.write(workflow_string_valid)
                    modified_files.append(repo_path + "/.github/workflows/" + workflow_dict[rosdistro])
        else:
            if not os.path.exists(repo_path + "/.github/workflows/"):
                os.makedirs(repo_path + "/.github/workflows/")
            with open(repo_path + "/.github/workflows/" + workflow_dict[rosdistro], mode='w') as f:
                f.write(workflow_string_valid)
                modified_files.append(repo_path + "/.github/workflows/" + workflow_dict[rosdistro])
        if len(modified_files) != 0:
            for modified_file in modified_files:
                modified_file = modified_file.replace("./ros_packages/"+package+"/","")
                git_repo.git.add(modified_file)
                git_repo.git.commit(modified_file, message='update ' + modified_file)
            if send_pr:
                git_repo.git.push('origin', branch)
                repo.create_pull(title="update CI workflow for " + rosdistro, body="update CI workflow", head=branch, base=repo.default_branch)
            else:
                print(colored(workflow_dict[rosdistro] + 'is defferent from template, but pass sending pull request, please call send_pr=true', 'red'))
        else:
            print(colored(workflow_dict[rosdistro] + ' is matched to the template', 'green'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='scripts for getting issues')
    parser.add_argument('token', help='token of the github')
    parser.add_argument('yaml_path', help='path to the packages.yaml file')
    parser.add_argument('send_pr', help='sending pull request or not', type=bool)
    args = parser.parse_args()
    check_ros_packages(args.token, args.yaml_path, args.send_pr)
