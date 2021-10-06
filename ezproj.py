#!/usr/bin/env python3

import subprocess, sys

#=======================================================================

def command_selector(project_type, project_name):
    project_command = []
    
    match project_type:
        case "angular" | "a" | "ang" | "ng":
            project_command = ["ng", "new", project_name, "--routing=true", "--style=css"]
        case "react" | "r":
            project_command = ["npx", "create-react-app", project_name]
        case "svelte" | "s" | "sv":
            project_command = ["npx", "degit", "sveltejs/template", project_name]

    return project_command

def create_project(project_type, project_name):
    try:
        subprocess.run(command_selector(project_type, project_name), shell=True)
        subprocess.run(["code", "./"+project_name], shell=True)
    except subprocess.CalledProcessError as err:
        print(err)

#=======================================================================

def main():
    create_project(sys.argv[1], sys.argv[2])

main()

#TODO perform checking on input
#TODO create tests
    # when given no arguments, a message should be displayed informing the user what arguments to pass
    # when given an invalid project type, a message should be displayed telling the user which projects they can create
    # when given a project name that already exists as a directory, a message should be displayed notifying the user that it already exists
    # when given a valid project type, but the user does not have the necessary requirements installed, then the user should be given a message telling them what they need to install