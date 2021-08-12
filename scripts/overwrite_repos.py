import argparse
import yaml
import sys

def overwrite(repos_filepath, overwrite_package, commit_hash):
    yaml_value = {'repositories' : {}}
    with open(repos_filepath) as file:
        repos_yaml = yaml.safe_load(file)
        for repository in repos_yaml['repositories']:
            package_name = repository.split("/")[-1]
            if package_name == overwrite_package:
                data = repos_yaml['repositories'][repository]
                data['version'] = commit_hash
                yaml_value['repositories'][repository] = data
            else:
                data = repos_yaml['repositories'][repository]
                yaml_value['repositories'][repository] = data
    print(yaml_value)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='python script for overwriting repos file')
    parser.add_argument('repos_filepath', help='path to the repos file')
    parser.add_argument('overwrite_package', help='target package to overwrite')
    parser.add_argument('commit_hash', help='commit hash of the target package')
    args = parser.parse_args()
    if args.overwrite_package == '':
        sys.exit(0)
    else:
        overwrite(args.repos_filepath, args.overwrite_package, args.commit_hash)