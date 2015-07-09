import os
import sys
from fnmatch import fnmatch

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def grep(filepath, keyword):
    file = open(filepath)
    try:
        for line_number, line in enumerate(file, start=1):
            if keyword in line:
                yield line_number, line
    except UnicodeDecodeError:
        pass


def get_files(search_dir):
    for currect_dir, dirs, files in os.walk(search_dir):
        yield from ((currect_dir, file) for file in files)


def file_filter(pattern, files):
    for path, name in files:
        if fnmatch(name, pattern):
            yield path, name


def files_grep(pattern, keyword, root):
    all_files = get_files(root)  # returns (path, filename)
    for path, name in file_filter(pattern, all_files):
        filepath = os.path.join(path, name)
        yield from ((filepath, n, t) for n, t in grep(filepath, keyword))


def get_matched_lines(pattern, keyword, root=SCRIPT_DIR):
    for filename, number, line in files_grep(pattern, keyword, root):
        yield "{}:{}: {}".format(filename,
                                 number,
                                 line.rstrip())


if __name__ == '__main__':
    _, pattern, word = sys.argv
    for line in get_matched_lines(pattern, word):
        print(line)
