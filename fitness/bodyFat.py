def calculateGoalWeight(weight, currentBF, goalBF) :
    check(weight, currentBF, goalBF)

    leanWeight = weight * (1 - currentBF)
    goalWeight = leanWeight / (1 - goalBF)

    return goalWeight


def check(weight, currentBF, goalBF) :
    pass