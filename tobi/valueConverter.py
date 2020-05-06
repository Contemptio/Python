"""
    @author Zimon Kuhs
    @date   2020-01-27
"""

import ast, getopt, sys

DEFAULT_VALUES = [
    1000,
    500,
    200,
    100,
    50,
    20,
    10,
    5,
    1
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

def printResult(result) :
    formatting = '%' + str(len(str(max(values))) + 1) + 'i'

    for key, value in result.items() :
        print((formatting + " : " + formatting) % (key, value))

def getOpts(argv) :
    myopts = getopt.getopt(argv, "v:")[0]
    result = {}

    for opt, arg in myopts :
        func = 0

        if opt == "-v" :
            func = toInts
        else :
            error("Invalid program argument %s." % opt)

        result[opt] = func(arg)

    return DEFAULT_VALUES if "-v" not in result else result

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
    numArgs = len(sys.argv)
    values = DEFAULT_VALUES

    if numArgs <= 1 :
        error("Usage: <value> [-v [amounts]]")

    value = toInt(sys.argv[1])

    if numArgs >= 3 :
        opts = getOpts(sys.argv[2:])
        values = opts["-v"]
    if numArgs >= 5 :
        error("Usage: <value> [-v [amounts]]")

    result = partition(value, values)
    printResult(partition(value, values))