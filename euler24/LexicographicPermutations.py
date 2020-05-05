"""
    @author Zimon Kuhs
    @answer ?
    @date   2020-01-23
"""

import sys

def collectPermutations(string, permutations, i, length) :

    if i >= length - 1 :
        permutations.append(string)
    else :
        for j in range(i, length - 1) :
            string = swap(string, i, j)
            collectPermutations(string, permutations, i + 1, length)
            string = swap(string, i, j)

def swap(string, pos1, pos2) :
    result = ""
    print(string)

    for i in range(0, len(string) - 1) :
        if i == pos1 :
            toAdd = string[pos2]
        elif i == pos2 :
            toAdd = string[pos1]
        else :
            toAdd = string[i]
        result = result + toAdd

    return result

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :
    args = sys.argv

    if len(args) >= 2 :
        print("Usage: py LexicographicPermutations.py.")

    string = "0123456789"
    permutations = []
    collectPermutations(string, permutations, 0, len(string))
