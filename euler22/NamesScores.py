"""
    @author Zimon Kuhs
    @answer ?
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
        error("Could not access file: %s" % str(exception))
    finally :
        openedFile.close()

    return lines

def getNames(string) :
    names = string.split("\",\"")
    names[0] = names[0].replace("\"", "")

    lastPos = len(names) - 1
    names[lastPos] = names[lastPos].replace("\"", "")

    return names

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

    print(len(names))