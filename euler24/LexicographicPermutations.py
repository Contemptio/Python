"""
    @author Zimon Kuhs
    @answer ?
    @date   2020-01-23
"""

import sys

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :
    args = sys.argv

    if len(args) != 3 :
        print("Usage: py LexicographicPermutations.py <beginning integer> <ending integer>.")