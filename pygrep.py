import os
import sys
from fnmatch import fnmatch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def grep_file(file, keyword):
    for number, line in enumerate(file, start=1):
        if keyword in line:
            yield number, line

def get_filepath(root, filenames):
    for filename in filenames:
        yield os.path.join(root, filename)


def get_file(filenames):
    for filename in filenames:
        yield open(filename), filename

def get_matches(filename_pattern):
    for root, dirs, files in os.walk(SCRIPT_DIR):
        # Filtering files by matching a pattern
        yield filter(lambda x: fnmatch(x, filename_pattern), files)


def grep(filename_pattern, keyword):
    for root, dirs, files in os.walk(SCRIPT_DIR):
        # Filtering files by matching a pattern
        matched_files = filter(lambda x: fnmatch(x, filename_pattern), files)

        for file, filename in get_file(get_filepath(root, matched_files)):
            try:
                for number, line in grep_file(file, keyword):
                    print("{}:{}: {}".format(
                        filename,
                        number,
                        line.rstrip()
                    ))
            except UnicodeDecodeError:
                    print(filename, "seems to be binary, skipping")


if __name__ == '__main__':
    _, pattern, word = sys.argv
    grep(pattern, word)
