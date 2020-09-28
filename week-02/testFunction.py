import math


def testFunction(x):
    if x < -2 or x > 5:
        return 0
    return math.cos(x) * (x ** 2 - 2 * x - 2.5) + (-0.4 * x + 2.5)
