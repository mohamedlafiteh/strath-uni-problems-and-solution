#!/usr/bin/env python3

def sets(setValues):
    print(">> Start of sets")
    print(setValues)

    setValues.pop()
    print(setValues)

    setValues.add("Randomise")

    print(">> End of sets")

if __name__ == "__main__":
    setValues = { "Query", "Sort", "Save"}
    copySet = setValues.copy()

    print("Set values before: " + str(setValues))
    sets(setValues)
    print("Set values after: " + str(setValues))
    print("Copy of original set: " + str(copySet))