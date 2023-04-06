import sys
import os
import subprocess

executable_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
if os.path.basename(executable_dir) == "src":
    executable_dir = os.path.join(executable_dir, os.path.pardir)

github_org_url = "https://github.com/PhitNest/"

projects = ["phitnest-api", "phitnest-app", "phitnest-core", "phitnest-cli"]


def pull():
    has_specific_projects = len(sys.argv) > 2
    for project_name in projects:
        if (not has_specific_projects) or project_name in sys.argv[2:]:
            repo_path = os.path.normpath(
                os.path.join(executable_dir, project_name))
            mono_index = os.path.normpath(os.path.join(
                repo_path, ".mono"))
            has_repo = os.path.exists(mono_index)
            repo_url = github_org_url + project_name + ".git"
            if has_repo:
                print("Pulling " + project_name)
                git_dir = os.path.join(repo_path, ".git")
                subprocess.run(["git", "--git-dir=" + git_dir,
                                "--work-tree=" + repo_path, "pull"])
            else:
                print("Cloning " + project_name)
                subprocess.run(["git", "clone", repo_url, repo_path]),


def api():
    subprocess.run(["sh", "build_tool.sh", " ".join(sys.argv[2:])], cwd=os.path.normpath(os.path.join(executable_dir,
                                                                                                      "phitnest-api", "build_tools")))


def print_help():
    print("Usage: phitnest <command> [options]")
    print("Commands:")
    print(
        "phitnest pull [projects] - Pulls all projects or the specified projects")
    print("phitnest api [options] - Runs the API build tool")


def main():
    if len(sys.argv) == 1:
        print_help()
    elif sys.argv[1] == "pull":
        pull()
    elif sys.argv[1] == "api":
        api()
    else:
        print_help()


if __name__ == "__main__":
    main()
