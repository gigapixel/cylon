#!/usr/bin/env python

import os
import sys
import textwrap

import subprocess

from .sublime import *


def run_shell(command, options=""):
    return subprocess.call("%s %s" % (command, options), shell=True)


def get_options_string(options):
    command = ""

    for option in options:
        if "=" in option:
            name = option.split('=')[0].strip()
            value = option.split('=')[1].strip()
            option = '--%s="%s"' % (name, value)
        else:
            option = '--%s' % option
        command = "%s %s" % (command, option)

    return command


def create_file(target, filename, content=""):
    if not os.path.exists(target):
        print("Not found %s directory." % target)
        return True

    if os.path.exists("%s/%s" % (target, filename)):
        print("File is already exists.")
        return True

    new_file = open("%s/%s" % (target, filename), 'w')
    new_file.write(content)
    new_file.close()


def init_project():
    os.makedirs("repositories")
    os.makedirs("features/steps")
    create_file()



def print_instruction():
    content = """
    Usage:
    cylon <command> [options]

    Commands:
    init                      Initialize project directories.
    run [options]             Run with specified options,
                              if omit options it will run all feature.
    Options:
    tags=<tags>               Run only feature/scenario associated with specified tags.
    """
    print(content)


def main():
    if len(sys.argv) == 1:
        print_instruction()
        return

    command = sys.argv[1].lower()

    if command == 'init':
        os.makedirs("repositories")
        os.makedirs("features/steps")

    elif command == 'sublime-setup':
        sublime.setup()

    elif command == 'run':
        if len(sys.argv) == 2:
            return run_shell("behack --quiet --no-skipped")
        else:
            args = sys.argv[2:]
            options = get_options_string(args)
            print(args)
            return run_shell("behack --quiet --no-skipped", options)
