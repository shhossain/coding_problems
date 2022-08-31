import os
import time
import subprocess


def check_time_file(file_path, language):
    if language == 'python':
        command = 'python ' + file_path
    elif language == 'cpp':
        file_dir = os.path.dirname(file_path)
        command = f"cd '{file_dir}' && g++ '{file_path}' -o test && ./test"
    else:
        print('Language not supported')
        return

    print(command)
    start = time.time()
    subprocess.call(command, shell=True)
    end = time.time()
    return end - start


def main():
    file_path = input('Enter file path: ')
    language = input('Enter language: ')
    time = check_time_file(file_path, language)
    print('Time: ', round(time, 2))


if __name__ == '__main__':
    main()
