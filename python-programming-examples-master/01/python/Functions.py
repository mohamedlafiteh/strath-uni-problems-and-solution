#!/usr/bin/env python3

def func1(stringValue):
    returnValue = func2(stringValue)
    print(returnValue)

def func2(stringValue):
    return stringValue

def main():
    func1("Functions")

if __name__ == "__main__":
    main()
