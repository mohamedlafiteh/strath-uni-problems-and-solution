#!/usr/bin/env python3

def booleanVariable(booleanValue):
    booleanValue = True
    booleanValue &= False
    print("booleanValue = " + str(booleanValue))

    booleanValue = True | False
    print("booleanValue = " + str(booleanValue))

    booleanValue = 1 > 0
    print(booleanValue)

if __name__ == "__main__":
    booleanValue = False
    booleanVariable(booleanValue)
    print("booleanValue = " + str(booleanValue))
