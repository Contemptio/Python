"""
    @author Zimon Kuhs
    @answer ?
    @date   2020-01-24
"""

import getopt, sys

KG_PER_LB = 0.4535924
LB_PER_KG = 2.204623
DEFAULT_KCAL = int(15 * LB_PER_KG)
DEFAULT_RATIO = 0.75
DEFAULT_UNIT = "kg"
KCAL_CARBS = 4
KCAL_FAT = 4
KCAL_FIBER = 2
KCAL_PROTEIN = 4
RATIO = 0.75

def macros(weight, opts) :
    calories = int(toInt(opts["kcal"]) * weight * toFloat(opts["ratio"]))
    fat = weight // 2
    fiber = calories * 0.014
    protein = weight
    carbs = (calories - (fat * KCAL_FAT + fiber * KCAL_FIBER + protein * KCAL_PROTEIN)) // 4

    return {
        "Calories" : int(calories),
        "Fat" : int(fat),
        "Carbohydrates" : int(carbs),
        "Protein" : int(protein),
        "Fiber" : int(fiber)
    }

def getOpts(argv) :
    myopts, args = getopt.getopt(argv[2:], "k:r:u:")
    result = {
        "kcal" : DEFAULT_KCAL,
        "ratio" : DEFAULT_RATIO,
        "unit" : DEFAULT_UNIT
    }

    for opt, arg in myopts :
        key = ""

        if opt == "-k" :
            key = "kcal"
        elif opt == "-r" :
            key = "ratio"
        elif opt == "-u" :
            key = "unit"

        result[key] = arg

    return result

def convertWeight(weight, unit) :
    if unit == "kg" :
        return weight
    if unit != "lb" :
        error("Invalid unit: %s." % unit)

    return weight * KG_PER_LB

def toFloat(number) :
    try :
        return float(number)
    except Exception as e :
        error("Expected a floating number, got " + str(number) + ": " + str(e))

def toInt(number) :
    try :
        return int(number)
    except Exception as e :
        error("Expected a floating number, got " + str(number) + ": " + str(e))

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :
    numArgs = len(sys.argv)

    if numArgs <= 1 :
        error("Usage: py LexicographicPermutations.py <weight> [<opts>]")

    opts = getOpts(sys.argv)
    weight = toFloat(sys.argv[1])
    macros = macros(convertWeight(weight, opts["unit"]), opts)

    print(macros)