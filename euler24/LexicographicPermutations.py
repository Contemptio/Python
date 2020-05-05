"""
    @author Zimon Kuhs
    @answer ?
    @date   2020-01-23
"""

import sys
from util.general import error, NotYetImplemented
from util.string import swapChars

def collectPermutations(string, permutations, i, length) :

    if i >= length - 1 :
        permutations.append(string)
    else :
        for j in range(i, length - 1) :
            string = swapChars(string, i, j)
            collectPermutations(string, permutations, i + 1, length)
            string = swapChars(string, i, j)

def findPermutations(string) :
    if 1 is 1 :
        raise NotYetImplemented()

    permutations = []
    collectPermutations(string, permutations, 0, len(string))

if __name__ == "__main__" :
    args = sys.argv

    if len(args) >= 2 :
        error("Usage: py LexicographicPermutations.py.")

    print(findPermutations("0123456789"))
