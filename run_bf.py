import sys

from fitness.bodyFat import calculateGoalWeight
from util import error, toFloat

if __name__ == "__main__" :
    argv = sys.argv
    argc = len(argv)

    if argc != 4 :
        error("Usage: py bodyFat.py <weight> <body fat%> <goal body fat%>")

    weight = toFloat(argv[1])
    currentBF = toFloat(argv[2])
    goalBF = toFloat(argv[3])

    print(calculateGoalWeight(weight, currentBF, goalBF))