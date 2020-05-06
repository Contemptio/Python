import sys

from util import error

if __name__ == "__main__" :
    argv = sys.argv
    argc = len(argv)

    if argc != 2 :
        error("Usage: py run_euler.py <test number>")