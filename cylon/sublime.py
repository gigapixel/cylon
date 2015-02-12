import os
import re
import glob
import zipfile

import getpass
import platform


class sublime:

    @classmethod
    def setup(cls):
        print("sublime setup...")

        package_dir = cls.get_package_dir()
        current_dir = cls.get_current_dir()

        print("building syntax...")
        source_dir = os.path.join(current_dir, "plugins/sublime/syntax")
        cls.build_package("Gherkin.sublime-package", source_dir, package_dir)

        print("building autocomplete...")
        stepfiles = [os.path.join(current_dir, 'steps/basic.py')]
        outfile = os.path.join(current_dir, 'plugins/sublime/autocomplete/cylon.sublime-completions')
        cls.generate_completion_file(stepfiles, outfile)

        source_dir = os.path.join(current_dir, "plugins/sublime/cylon-steps")
        cls.build_package("Cylon.sublime-package", source_dir, package_dir)

        print("setup completed.")


    @classmethod
    def build_package(cls, name, source, target):
        target = os.path.join(target, name)
        package = zipfile.ZipFile(target, 'w')

        for root, dirs, files in os.walk(source):
            for file in files:
                package.write(os.path.join(root, file))
        package.close()


    @classmethod
    def get_current_dir(cls):
        return os.path.dirname(os.path.realpath(__file__))


    @classmethod
    def get_package_dir(cls):
        user = getpass.getuser()
        system = platform.system()

        target = ""
        if system == "Windows":
            target = "Users/" + user + "/AppData/Roaming"
        elif system == "Darwin":
            target = "/Users/" + user + "/Library/Application Support"
        target += "/Sublime Text 3/Installed Packages"

        return target


    @classmethod
    def generate_completion_file(cls, stepfiles, outfile):
        content = []
        content.append('{\n')
        content.append('\t"scope": "source.feature",\n')
        content.append('\t"completions":\n')
        content.append('\t[\n')

        for stepfile in stepfiles:
            steps = cls.extract_steps(stepfile)
            for step in steps[:-1]:
                content.append('\t\t"' + step + '",\n')
            content.append('\t\t"' + steps[-1] + '"\n') ## last item without ','

        content.append('\t]\n')
        content.append('}\n')

        textfile = open(outfile, "w")

        for line in content:
            textfile.write(line)

        textfile.close()


    @classmethod
    def extract_steps(cls, filename):
        f = open(filename)
        lines = f.readlines()
        f.close()

        steps = []

        for line in lines:
            if line.strip().startswith("@step"):
                step = cls.extract_step(line)
                step = cls.place_step_arguments(step)
                steps.append(step)

        return steps


    @classmethod
    def extract_step(cls, line):
        if '("' in line:
            regex = '"([^"]*)"'
        elif "('" in line:
            regex = "'([^'']*)'"

        matches = re.findall(regex, line)
        step = matches[0]

        return step


    @classmethod
    def place_step_arguments(cls, step):
        regex = "({[A-Za-z0-9_]*})"
        matches = re.findall(regex, step)

        for index, match in enumerate(matches):
            arg = "${%d:%s}" % ((index + 1), match[1:-1].strip())
            step = step.replace(match, arg)

        return step
