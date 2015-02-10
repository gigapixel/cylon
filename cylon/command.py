#!/usr/bin/env python

import os
import sys
import textwrap

import subprocess


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


def run_shell(command, options=""):
    return subprocess.call("%s %s" % (command, options), shell=True)


def main():
    if len(sys.argv) == 1:
        print("invalid command.")
        return

    command = sys.argv[1].lower()

    if command == 'init':
        os.makedirs("pages")
        os.makedirs("features/steps")

    elif command == 'run':
        if len(sys.argv) == 2:
            return run_shell("behack --quiet --no-skipped")
        else:
            args = sys.argv[2:]
            options = get_options_string(args)
            print(args)
            return run_shell("behack --quiet --no-skipped", options)
