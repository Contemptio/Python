"""
    @author Zimon Kuhs
    @answer ?
    @date   2020-01-24
"""

import sys

KG_PER_LB = 0.4535924
LB_PER_KG = 2.204623
KCAL_CARBS = 4
KCAL_FAT = 4
KCAL_FIBER = 2
KCAL_PROTEIN = 4
RATIO = 0.75

def toNumber(string) :
    try :
        return float(string)
    except Exception as e :
        error("Error, %s has to be a floating point number: %s" % (string, str(e)))

def convert(number, arg) :
    if arg[0] == "k" or arg == "kg" :
        return number
    if arg[0] == "l" or arg == "lb" :
        return KG_PER_LB * number

    error("Invalid weight type %s." % arg)

def macros(weight, kcalPerKg) :
    calories = int(kcalPerKg * weight * RATIO)
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

def error(message) :
    print(message)
    sys.exit(1)

if __name__ == "__main__" :
    args = sys.argv
    numArgs = len(args)

    weight = 0

    # TODO: Convert to input arg.
    kcalPerKg = int(15 * 2.204623)

    if numArgs <= 1 or numArgs > 3 :
        error("Usage: py LexicographicPermutations.py <weight> [kg || lb]")
    if numArgs >= 2 :
        weight = toNumber(args[1])
    if numArgs == 3 :
        weight = convert(weight, toNumber(args[2]))

    macros = macros(weight, kcalPerKg)

    print(macros)