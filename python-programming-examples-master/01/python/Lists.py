#!/usr/bin/env python3

def lists(listValues):
    print(">> Start of lists")

    del listValues[:]

    listValues += [ 15.0 ]
    print(listValues)

    listValues.pop()
    print(listValues)

    listValues += range(5)
    print(listValues)

    listValues += range(4)
    listValues.sort()
    print(">> End of lists")

if __name__ == "__main__":
    listValues = [0]*2

    copyList = listValues.copy()

    print("List values before: " + str(listValues))
    lists(listValues)
    print("List values after: " + str(listValues))
    print("Copy of original list: " + str(copyList))

    print("The list contains " + str(len(listValues)) + " elements.")
    print("The third element: " + str(listValues[2]))
    print("The last element: " + str(listValues[-1]))
    print("The fourth and fifth elements: " + str(listValues[5:7]))