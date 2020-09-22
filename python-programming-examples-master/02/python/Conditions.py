#!/usr/bin/env python3

def returnsNone():
    return

def conditionalOutput(inputValue):
    if inputValue > 0:
        return inputValue * 2
    return None

def valueInList(inputList, value):
    if value in inputList:
        return value

def powerState(powerName):
    powerValue = 0
    if powerName == "On":
        powerValue = 1
    elif powerName == "Off":
        powerValue = 0
    else:
        return None
    return powerValue

def ipAddress(machineName):
    addresses = {}
    addresses["localhost"] = "127.0.0.1"
    addresses["GoogleDNS"] = "8.8.8.8"
    if machineName in addresses:
        return addresses[machineName]
    return None

def notNone(value):
    return not value is None

def notZero(value):
    return value != 0

def conditions():
    if returnsNone() is None:
        print("returnsNone returned None")

    inputValue = 2
    print("conditionalOutput(" + str(inputValue) + ") = " + str(conditionalOutput(inputValue)))

    inputValue = -1
    print("conditionalOutput(" + str(inputValue) + ") = " + str(conditionalOutput(inputValue)))

    powerName = "On"
    print("powerState(\"" + powerName + "\") = " + str(powerState(powerName)))

    machineName = "localhost"
    print("ipAddress(\"" + machineName + "\") = \"" + str(ipAddress(machineName)) + "\"")

    value = None
    print("notNone(" + str(value) + ") = " + str(notNone(value)))

    value = -5
    print("notZero(" + str(value) + ") = " + str(notZero(value)))

if __name__ == "__main__":
    conditions()