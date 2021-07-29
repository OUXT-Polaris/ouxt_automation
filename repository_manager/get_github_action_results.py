import argparse
from github import Github
import yaml

def get_ros_ci_results(token, yaml_path):
    g = Github(token)
    data = []
    workflow_dict = {"galactic" : "ROS2-Galactic.yaml", "foxy" : "ROS2-Foxy.yaml", "dashing" : "ROS2-Dashing.yaml"}
    with open(yaml_path) as file:
        config = yaml.safe_load(file)
        for user in config["ros"]:
            for package in config["ros"][user]:
                url = "https://github.com/" + user + "/" + package + ".git"
                support_platforms = []
                if config["ros"][user][package] is None:
                    support_platforms = list(workflow_dict.keys())
                elif "rosdistro" not in config["ros"][user][package]:
                    support_platforms = list(workflow_dict.keys())
                else:
                    support_platforms = config["ros"][user][package]["rosdistro"]
                print("scanning -> " + url)
                repo = g.get_repo(user + "/" + package)
                package_status = [package]
                for rosdistro in workflow_dict:
                    if rosdistro in support_platforms:
                        try:
                            print(rosdistro)
                            workflow = repo.get_workflow(workflow_dict[rosdistro])
                            print(workflow)
                            package_status.append(str("![" + package + "](" + workflow.badge_url + ")"))
                        except:
                            package_status.append("<span style=\"color: red; \">No Test for " + rosdistro + ".</span>")
                    else:
                        package_status.append("No " + rosdistro + " support.")
                data.append(package_status)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='scripts for getting issues')
    parser.add_argument('token', help='token of the github')
    parser.add_argument('yaml_path', help='path to the packages.yaml file')
    args = parser.parse_args()
    data = get_ros_ci_results(args.token, args.yaml_path)
    print(data)