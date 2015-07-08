import os
import sys
from fnmatch import fnmatch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def grep_file(file, keyword):
    for number, line in enumerate(file, start=1):
        if keyword in line:
            yield number, line


def grep(filename_pattern, keyword):
    for root, dirs, files in os.walk(SCRIPT_DIR):
        # Filtering files by matching a pattern
        matched_files = filter(lambda x: fnmatch(x, filename_pattern), files)

        for filename in matched_files:

            file_fullpath = os.path.join(SCRIPT_DIR, root, filename)
            with open(file_fullpath) as file:
                try:
                    for number, line in grep_file(file, keyword):
                        print("{}:{}: {}".format(file_fullpath, number, line.rstrip()))
                except UnicodeDecodeError:
                    print(file_fullpath, " seems to be binary, skipping")


if __name__ == '__main__':
    _, pattern, word = sys.argv
    grep(pattern, word)
