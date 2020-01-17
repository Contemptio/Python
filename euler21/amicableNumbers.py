"""
    @author Zimon Kuhs
    @date   2020-01-17
"""

import sys

def evenDivisors(nominator) :
    result = []

    for denominator in range(1, nominator) :
        if nominator % denominator == 0 :
            result.append(denominator)

    return result

def findAmicablePairs (target) :
    numberToSum = {}

    for i in range(1, target) :
        divisorSum = sum(evenDivisors(i))

        if divisorSum < target:
            numberToSum[i] = divisorSum

    pairSet = set()
    for key, value in numberToSum.items() :

        if  key == value \
            or value <= 0 or value > target \
            or value not in numberToSum \
            or key == value \
            or not numberToSum[value] == key :

            continue

        pairSet.add(key)
        pairSet.add(value)

    return sum(pairSet)

def error(message) :
    print(message)
    sys.exit(1)

def toInteger(string):
    try: 
        return int(string)
    except ValueError:
        error("Expected integer string, found: " + string + ".")

if __name__ == "__main__" :
    if len(sys.argv) != 2 :
        error("Usage: amicableNumbers.py <top number>")

    number = toInteger(sys.argv[1])

    print(findAmicablePairs(number))