"""
    @author Zimon Kuhs
    @answer 31626
    @date   2020-01-17
"""

import sys
from util.general import *

def evenDivisors(nominator) :
    result = []

    for denominator in range(1, nominator) :
        if nominator % denominator == 0 :
            result.append(denominator)

    return result

def findAmicablePairs (target) :
    numberToSum = {}

    for i in range(1, target) :
        if i in numberToSum :
            continue

        divisorSum1 = sum(evenDivisors(i))
        divisorSum2 = sum(evenDivisors(divisorSum1))

        if divisorSum1 == divisorSum2 :
            continue

        if divisorSum1 < target :
            numberToSum[i] = divisorSum1

            if divisorSum2 < target :
                numberToSum[divisorSum1] = divisorSum2

    pairSet = set()
    for key, value in numberToSum.items() :

        if  value in numberToSum \
            and numberToSum[value] == key :

            pairSet.add(key)
            pairSet.add(value)

    return sum(pairSet)

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        error("Usage: amicableNumbers.py <top number>")

    print(findAmicablePairs(toInteger(sys.argv[1])))