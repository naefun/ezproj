#!/usr/bin/env python3

import subprocess, sys

#=======================================================================

def command_selector(project_type, project_name, path_prefix):
    project_command = []
    
    match project_type:
        case "angular" | "a" | "ang" | "ng":
            project_command = ["ng", "new", project_name, "--routing=true", "--style=css"]
        case "react" | "r":
            project_command = ["npx", "create-react-app", path_prefix+project_name]
        case "svelte" | "s" | "sv":
            project_command = ["npx", "degit", "sveltejs/template", path_prefix+project_name]

    return project_command

def create_project(project_type, project_name, path_prefix):
    try:
        subprocess.run(command_selector(project_type, project_name, path_prefix), shell=True)
        subprocess.run(["code", project_name], shell=True)
    except subprocess.SubprocessError as err:
        print(err)

def fix_path(path):
    fixed_path = ""
    for i in path:
        if i == "\\":
            fixed_path += "/"
        else:
            fixed_path += i
    return fixed_path
#=======================================================================

def main():
    project_type = sys.argv[1]
    project_name = sys.argv[2]
    path = fix_path(sys.argv[3])
    path_prefix = path+"/"

    create_project(project_type, project_name, path_prefix)

main()

#TODO perform checking on input
#TODO create tests
    # when given no arguments, a message should be displayed informing the user what arguments to pass
    # when given an invalid project type, a message should be displayed telling the user which projects they can create
    # when given a project name that already exists as a directory, a message should be displayed notifying the user that it already exists
    # when given a valid project type, but the user does not have the necessary requirements installed, then the user should be given a message telling them what they need to install