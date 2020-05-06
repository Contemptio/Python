"""
    @author Zimon Kuhs
    @date   2020-01-27
"""

import ast, getopt, sys

TOWNS = [
    "Castle",
    "Conflux",
    "Cove",
    "Dungeon",
    "Fortress",
    "Inferno",
    "Necropolis"
    "Rampart",
    "Stronghold",
    "Tower"
]

def partition(value, values) :
    sortedValues = sorted(values, key = int, reverse = True)

    i = 0
    result = {}

    while value > 0 :
        segment = sortedValues[i]
        result[segment] = value // segment
        value = value - result[segment] * segment
        i = i + 1

    return result

def printResult(result, values) :
    formatting = '%' + str(len(str(max(values))) + 1) + 'i'

    for key, value in result.items() :
        print((formatting + " : " + formatting) % (key, value))

def toInt(number) :
    try :
        return int(number)
    except Exception as e :
        error("Expected an integer, got %s: %s." % (str(number), str(e)))

def toInts(string) :
    try :
        return ast.literal_eval(string)
    except Exception as e :
        error("Invalid list string provided as argument: %s." % str(e)) 

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :
    args = sys.argv

    if len(args) != 2 :
        error("Usage: python Heroes3.py <folder name>")