"""
    @author Zimon Kuhs
    @date   2020-01-24
"""

import getopt, sys

from . import error, toFloat, toInteger

KCAL_PER_MACRO = {
    "Carbohydrates" : 4,
    "Fat" : 9,
    "Fiber" : 2,
    "Protein" : 4
}

KG_PER_LB = 0.4535924
LB_PER_KG = 2.204623
DEFAULT_KCAL = int(15 * LB_PER_KG)
DEFAULT_RATIO = 0.75
DEFAULT_UNIT = "kg"
FIBER_PER_KCAL = 0.014
CARB_PER_KCAL = 1 / KCAL_PER_MACRO["Carbohydrates"]
FAT_PER_KCAL = 1 / KCAL_PER_MACRO["Fat"]

def macros(weight, opts) :
    macros = {}

    macros["Calories"] = int(toInteger(opts["kcal"]) * \
                weight * toFloat(opts["ratio"]))
    macros["Carbohydrates"] = 0
    macros["Fat"] = weight * (1 if opts["highFat"] else 0.5)
    macros["Fiber"] = macros["Calories"] * FIBER_PER_KCAL
    macros["Protein"] = weight * (2 if opts["highProtein"] else 1)
    print(opts)
    
    if opts["lowCarb"] :
        macros["Carbohydrates"] = 20
        macros["Fat"] = rest(macros, "Fat")
    else :
        macros["Carbohydrates"] = rest(macros, "Carbohydrates")

    for key, value in macros.items() :
        macros[key] = int(value)

    return macros

def rest(macros, macroKey) :
    calories = macros["Calories"]

    for key, value in macros.items() :
        if key != macroKey and key != "Calories" :
            calories = calories - KCAL_PER_MACRO[key] * value

    return calories / KCAL_PER_MACRO[macroKey]

def getOpts(argv) :
    myopts, args = getopt.getopt(argv[2:], "hf:hp:k:lc:r:u:")
    result = {
        "lowFat" : False,
        "highProtein" : False,
        "kcal" : DEFAULT_KCAL,
        "lowCarb" : False,
        "ratio" : DEFAULT_RATIO,
        "unit" : DEFAULT_UNIT
    }
    print(myopts)

    for opt, arg in myopts :
        key = ""
        func = 0

        if opt == "-hf" :
            key = "highFat"
            func = bool
        elif opt == "-hp" :
            key = "highProtein"
            func = bool
        elif opt == "-k" :
            key = "kcal"
            func = int
        elif opt == "-lc" :
            key = "lowCarb"
            func = bool
        elif opt == "-r" :
            key = "ratio"
            func = float
        elif opt == "-u" :
            key = "unit"
            func = str

        result[key] = func(arg)

    return result

def convertWeight(weight, unit) :
    if unit == "kg" :
        return weight
    if unit != "lb" :
        error("Invalid unit: %s." % unit)

    return weight * KG_PER_LB