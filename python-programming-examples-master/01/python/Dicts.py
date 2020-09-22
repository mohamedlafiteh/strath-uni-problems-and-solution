#!/usr/bin/env python3

def dicts(dictValues):
    print(">> Start of dicts")

    dictValues.clear()

    dictValues["localhost"] = "127.0.0.1"
    dictValues["googleDNS1"] = "8.8.8.8"
    dictValues["googleDNS2"] = "8.8.4.4"
    dictValues["myMachine"] = "192.168.1.66"
    print(dictValues)

    dictValues.pop("myMachine")
    print(dictValues)

    keys = list(dictValues.keys())
    print("Keys : " + str(keys))
    
    values = list(dictValues.values())
    print("Values : " + str(values))

    print(">> End of dicts")

if __name__ == "__main__":
    dictValues = {}
    dictValues["AnotherMachine"] = "10.0.0.12"

    copyDict = dictValues.copy()

    print("Dictionary values before: " + str(dictValues))
    dicts(dictValues)
    print("Dictionary values after: " + str(dictValues))
    print("Copy of original dictionary: " + str(copyDict))