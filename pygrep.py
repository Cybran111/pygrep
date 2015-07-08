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
            with open(os.path.join(SCRIPT_DIR, root, filename)) as file:
                for number, line in grep_file(file, keyword):
                    print("{}:{}: {}".format(filename, number, line.rstrip()))


if __name__ == '__main__':
    _, pattern, word = sys.argv
    grep(pattern, word)
