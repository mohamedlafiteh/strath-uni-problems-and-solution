#!/usr/bin/env python3

def stringVariables(stringValue):
    stringValue = "A value"
    print(stringValue)

    stringValue += ",Another value"
    print(stringValue)

    firstValue = "First value"
    stringValue = firstValue + "\t" + stringValue + "  \n" + "A new line."
    print(stringValue)

    stringValue = stringValue.replace("First","Primary")
    stringValue = stringValue.replace("\t",",")
    stringValue = stringValue.split("\n")[0]
    stringValue = stringValue.strip()
    print(stringValue)

    searchString = "value"
    print("The string \"" + searchString + "\" was found at index " + str(stringValue.find(searchString)))

if __name__ == "__main__":
    stringValue = ""
    stringVariables(stringValue)
    print("stringValue=\"" + stringValue + "\"")
    
