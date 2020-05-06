"""
    @author Zimon Kuhs
    @answer 4179871
    @date   2020-01-18
"""

from . import error, toInteger

def properDivisors(number) :
    result = set()

    i = 1
    while i * i <= number:
        if number % i == 0 :
            result.add(i)


            if number // i != i :
                result.add(number // i)
        i += 1
    result.remove(number)

    return result

def isAbundant(number) :
    return sum(properDivisors(number)) > number

def findAbundants(ceiling) :
    result = []

    for i in range(1, ceiling) :
        if isAbundant(i) :
            result.append(i)

    return result

def getSums(numbers, target) :
    result = set()

    for a in numbers :
        for b in numbers :
            theSum = a + b

            if theSum > target :
                break
            result.add(theSum)

    return result

def getMissing(numbers, target) :
    return  [i for i in range(1, target) if i not in numbers] 

def findNonAbundantSum(target) :
    abundants = findAbundants(target)
    abundantSums = getSums(abundants, target)
    return sum(getMissing(abundantSums, target))