"""
    @author Zimon Kuhs
    @answer 871198282
    @date   2020-01-18
"""

import os
import sys

def readNames(fileName) :
    lines = []

    try :
        openedFile = open(fileName, 'r')
        lines = openedFile.readlines()
    except IOError as exception :
        error("Unable to access file: %s" % str(exception))
    finally :
        openedFile.close()

    return lines

def getNames(string) :
    names = string.split("\",\"")
    names[0] = names[0].replace("\"", "")

    lastPos = len(names) - 1
    names[lastPos] = names[lastPos].replace("\"", "")

    return names

def score(name) :
    result = 0

    for c in name :
        result += (ord(c) - 64)

    return result

def scores(names) :
    result = []

    for i in range(0, len(names)) :
        result.append((i + 1) * score(names[i]))

    return result

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :
    args = sys.argv

    if len(args) != 2 :
        error("Usage: python NamesScores.py <file_name>")

    fileName = args[1]
    if not os.path.isfile(fileName) :
        error("No such file: %s" % fileName)

    names = readNames(fileName)
    names = getNames(names[0])
    nameScores = scores(sorted(names))

    print(sum(nameScores))