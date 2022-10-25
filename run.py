# run py and cpp files with input and output files
import subprocess
import os
import sys
# import time
import termcolor
import json
import re
import threading
from difflib import Differ


def cprint(*texts, color='green'):
    print(termcolor.colored(' '.join(texts), color))


class Run:
    def __init__(self, file_path) -> None:
        if ' ' in file_path:
            if not (file_path.startswith('"') and file_path.endswith('"')):
                file_path = f'"{file_path}"'

        self.file_path = file_path
        # self.file_type = os.path.splitext(file_path)[1].replace('"', '')

        run_file_path = os.path.abspath(__file__)
        self.run_folder = os.path.dirname(run_file_path)

        # CONFIG
        self.recent_file = "recent_file"
        # File "f:\Code\clones\coding_problems\run.py", line 2
        # impor subprocess
        self.python_error_rexp = r'File "(.+)", line (\d+)'
        self.run()

    @property
    def file_type(self):
        replace = ['"']
        file_type = os.path.splitext(self.file_path)[1]
        for r in replace:
            file_type = file_type.replace(r, '')
        return file_type

    @property
    def config_file_location(self):
        loc = os.path.join(self.run_folder, 'config.json')
        if not os.path.exists(loc):
            self.write_file(loc, '{}')
        return loc

    @property
    def input_file_location(self):
        return os.path.join(self.run_folder, 'inputf.txt')

    @property
    def output_file_location(self):
        return os.path.join(self.run_folder, 'outputf.txt')

    @property
    def exceped_output_file_location(self):
        return os.path.join(self.run_folder, 'eoutputf.txt')

    def config(self, key, value=None):
        if not value:
            return self.read_config(key)
        else:
            self.write_config(key, value)

    def read_config(self, key):
        with open(self.config_file_location, 'r') as f:
            data = json.load(f)
            return data.get(key, None)

    def write_config(self, key, value):
        with open(self.config_file_location, 'r') as f:
            data = json.load(f)
        data[key] = value
        with open(self.config_file_location, 'w') as f:
            json.dump(data, f)

    def read_file(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()

    def write_file(self, file_path, content):
        with open(file_path, 'w') as f:
            f.write(content)

    def append_file(self, file_path, content):
        with open(file_path, 'a') as f:
            f.write(content)

    def run(self):
        if self.file_type == '.py':
            self.run_py()
        elif self.file_type == '.cpp':
            self.run_cpp()
        else:
            recent_file = self.config(self.recent_file)
            if recent_file:
                Run(recent_file)
                return

        self.config(self.recent_file, self.file_path)

    def match_output(self, output, expected_output):
        olines = output.splitlines()
        elines = expected_output.splitlines()

        # remove empty lines
        olines = [line for line in olines if line]
        elines = [line for line in elines if line]

        if len(olines) != len(elines):
            return False

        for o, e in zip(olines, elines):
            # o, e = o.strip(), e.strip()
            if o != e:
                return False
        return True

    def get_diffrences(self, output, expected_output):
        d = Differ()
        diff = d.compare(output.splitlines(), expected_output.splitlines())
        # print diff if matched green otherwise red
        for line in diff:
            if line.startswith(' '):
                cprint(line, color='blue')
            elif line.startswith('-'):
                cprint(line, color='red')
            elif line.startswith('+'):
                cprint(line, color='green')

    def diff(self, str_output, eoutput):
        t = threading.Thread(target=self.get_diffrences, args=(
            str_output, eoutput), daemon=True)
        t.start()


    def run_py(self):
        cmd = f'python {self.file_path}'
        input_text = self.read_file(self.input_file_location)
        ibyte = bytes(input_text, 'utf-8')

        # run python file
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = p.communicate(input=ibyte)[0]
        str_output = str(output, 'utf-8')
        str_output = str_output.replace("\r", "")

        # check error
        error = re.findall(self.python_error_rexp, str_output)

        if error:
            cprint("Run python file failed", color='red')
            print(str_output)
            return

        self.write_file(self.output_file_location, str_output)
        # cprint("Run python file successfully", color='green')

        # check if we need to compare output
        eoutput = self.read_file(self.exceped_output_file_location)
        if eoutput:
            if self.match_output(str_output, eoutput):
                cprint("[+] Output matched", color='green')
            else:
                cprint("[-] Output not matched", color='red')
                self.diff(str_output, eoutput)


    def run_cpp(self):
        build_folder = os.path.join(self.run_folder, 'build')
        if not os.path.exists(build_folder):
            os.mkdir(build_folder)

        build_file = os.path.join(build_folder, os.path.basename(
            self.file_path).replace(".cpp", ""))

        cmd = f'g++ {self.file_path} -O3 -std=c++14 -o "{build_file}"'
        p = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = p.communicate()[0]
        str_output = str(output, 'utf-8')
        str_output = str_output.replace("\r", "")

        # check error
        if str_output:
            cprint("Build cpp file failed", color='red')
            print(str_output)
            return

        # cprint("Compile cpp file successfully", color='green')

        # run cpp file
        cmd = f'"{build_file}"'
        input_text = self.read_file(self.input_file_location)
        ibyte = bytes(input_text, 'utf-8')
        p = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = p.communicate(input=ibyte)[0]
        str_output = str(output, 'utf-8')
        str_output = str_output.replace("\r", "")
        self.write_file(self.output_file_location, str_output)
        # cprint("Run cpp file successfully", color='green')

        # check if we need to compare output
        eoutput = self.read_file(self.exceped_output_file_location)
        if eoutput:
            if self.match_output(str_output, eoutput):
                cprint("[+] Output matched", color='green')
            else:
                cprint("[-] Output not matched", color='red')
                self.diff(str_output, eoutput)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        cprint("Please input file path", color='red')
        exit()
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        cprint("File not exists", color='red')
        exit()
    Run(file_path)
