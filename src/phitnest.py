import sys
import os
import subprocess

executable_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
if os.path.basename(executable_dir) == "src":
    executable_dir = os.path.join(
        executable_dir, os.path.pardir, os.path.pardir)

github_org_url = "https://github.com/PhitNest/"

projects = ["api", "app", "core", "cli", "admin"]


def pull():
    has_specific_projects = len(sys.argv) > 2
    for project_name in projects:
        if (not has_specific_projects) or project_name in sys.argv[2:]:
            full_project_name = "phitnest-" + project_name
            repo_path = os.path.normpath(
                os.path.join(executable_dir, project_name))
            mono_index = os.path.normpath(os.path.join(
                repo_path, ".mono"))
            has_repo = os.path.exists(mono_index)
            repo_url = github_org_url + full_project_name + ".git"
            if has_repo:
                print("Pulling " + full_project_name)
                git_dir = os.path.join(repo_path, ".git")
                subprocess.run(["git", "--git-dir=" + git_dir,
                                "--work-tree=" + repo_path, "pull"])
            else:
                print("Cloning " + full_project_name)
                subprocess.run(["git", "clone", repo_url, repo_path]),


def api():
    subprocess.run(["sh", "build_tool.sh", " ".join(sys.argv[2:])], cwd=os.path.normpath(os.path.join(executable_dir,
                                                                                                      "phitnest-api", "build_tools")))


def git():
    if len(sys.argv) < 4:
        subprocess.run(["git", "--help"])
    else:
        full_project_name = "phitnest-" + sys.argv[1]
        subprocess.run(["git"] + sys.argv[3:], cwd=os.path.normpath(
            os.path.join(executable_dir, full_project_name)))


def print_help():
    print("Usage: phitnest <command> [options]")
    print("Commands:")
    print(
        "phitnest pull [projects]     - Pulls all projects or the specified projects")
    print("phitnest api [options]       - Runs the API build tool")
    print(
        "phitnest [project] git       - Runs git commands in a specific project")


def main():
    if len(sys.argv) == 1:
        print_help()
    elif sys.argv[1] == "pull":
        pull()
    elif sys.argv[1] == "api":
        api()
    elif sys.argv[1] in projects:
        if len(sys.argv) > 2 and sys.argv[2] == "git":
            git()
    else:
        print_help()


if __name__ == "__main__":
    main()
