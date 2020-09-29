import testFunction
import random
from testFunction import testFunction


def values_function():
    # iterating each number in list
    minimum = {}
    x = []
    y = []

    for i in range(-200, 500):
        x.append(float(i/100))

    for j in x:
        y_values = testFunction(j)
        y += [y_values]
        # y3 <y2 and y3 <y4

    for num in range(len(y) - 1):
        if num > 1:
            if y[num] < y[num - 1] and y[num] < y[num + 1]:
                minimum[x[num]] = y[num]

    newMinimaX = []
    for key in minimum.keys():
        newMinimaX += [key]

    newMinimaX.sort()

    return list(minimum.keys())


def random_number():

    three_random = []
    for i in range(3):
        three_random.append(random.uniform(-2., 5.))
    sorted_list = sorted(three_random)
    lowest_two = [sorted_list[0:2]]
    print(lowest_two)


random_number()
x = 1.5
y = values_function()

print(" testFunction ( " + str(x) + " ) = " + str(y))
