import random
import testFunction
from testFunction import testFunction

"""
A function to find minima by scanning several
points.
"""


def minimaFromScan(printPoints=False):
    minima = []
    lastPoint = 0.0
    previousLast = 0.0
    nPoints = 0
    x = -2
    stepSize = 0.01
    while x <= 5:
        y = testFunction(x)

        if printPoints:
            print("testFunction(" + str(x) + ") = " + str(y))

        x += stepSize
        nPoints += 1

        # For the first point, just store it.
        if nPoints == 1:
            lastPoint = y
            continue

        # Store the first and second point and continue.
        if nPoints == 2:
            previousLast = lastPoint
            lastPoint = y
            continue

        # If a minimum as been reached, store it.
        if y > lastPoint and lastPoint < previousLast:
            minima += [x - (stepSize * 2)]

        # Keep this point and the previous point.
        previousLast = lastPoint
        lastPoint = y

    return minima


"""
A function to find a minimum using random sampling.
"""


def minimumFromSampling():
    # Randomly select three values between the limits.
    xValues = []
    for i in range(3):
        xValues += [random.uniform(-2, 5)]

    # The x values must be sorted.
    xValues.sort()

    # Calculate the y values, using the test function.
    yValues = []
    for x in xValues:
        yValues += [testFunction(x)]

    # Find the minimum.
    while True:

        # Find the maximum value.
        iMax = yValues.index(max(yValues))

        # Take the limits from the two remaining values.
        iPoint = 0
        for i in range(3):

            # If this is the maximum point skip it.
            if i == iMax:
                continue

            # Prevent indexing outside list.
            if iPoint >= 3:
                break

            # Keep or overwrite values.
            xValues[iPoint] = xValues[i]
            yValues[iPoint] = yValues[i]

            # The next point to be kept should be
            # the third point.
            iPoint += 2

        # Check if the limits are close to each other.
        if abs(xValues[0] - xValues[2]) < 0.01:
            iMin = yValues.index(min([yValues[0], yValues[2]]))
            return xValues[iMin]

        # Generate a new value.
        xValues[1] = random.uniform(xValues[0], xValues[2])
        yValues[1] = testFunction(xValues[1])


if __name__ == "__main__":
    # print("Minima from scanning: " + str(minimaFromScan()))
    print("Minimum from sampling: " + str(minimumFromSampling()))