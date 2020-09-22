#!/usr/bin/env python3

import math

def numericVariables(firstValue, secondValue):
    firstValue = firstValue + 1
    firstValue += 1
    firstValue *= 2
    firstValue /= 3
    print(str(firstValue))

    firstValue = int(firstValue)
    print(firstValue)

    secondValue = math.cos(math.pi/2.)
    print(secondValue)

if __name__ == "__main__":
    firstValue = 0
    secondValue = 0.
    numericVariables(firstValue, secondValue)
    print("firstValue=" + str(firstValue) + ", secondValue=" + str(secondValue))
