import sys
import os
import subprocess

executable_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
cli_root_dir = os.path.join(executable_dir, os.path.pardir)
mono_root_dir = os.path.join(cli_root_dir, os.path.pardir)

github_org_url = "https://github.com/PhitNest/"


def pull_all():
    with open(os.path.join(cli_root_dir, "projects.txt"), "r") as f:
        project_name = f.readline().strip()
        while project_name != "":
            repo_path = os.path.normpath(
                os.path.join(mono_root_dir, project_name))
            mono_index = os.path.normpath(os.path.join(
                repo_path, ".mono"))
            has_repo = os.path.exists(mono_index)
            repo_url = github_org_url + project_name + ".git"
            if has_repo:
                print("Pulling " + project_name)
                subprocess.run(
                    ["git", "pull", repo_url]),
            else:
                print("Cloning " + project_name)
                subprocess.run(["git", "clone", repo_url, repo_path]),
                with open(mono_index, "w") as mono_file:
                    mono_file.write(
                        "This is a mono repo index file. Do not delete it.")
            project_name = f.readline()


def print_help():
    print("Usage: phitnest <command> [options]")


def main():
    if len(sys.argv) == 1:
        print_help()
    else:
        pull_all()


if __name__ == "__main__":
    main()
