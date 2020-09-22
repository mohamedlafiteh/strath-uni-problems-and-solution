#!/usr/bin/env python3

import pickle

class DataObject():
    def __init__(self):
        self.__private = "DataString:12345"

    def __str__(self):
        return "{ __private=" + str(self.__private) + "}"

def writePickle(fileName):
    dataObject = DataObject()
    outputFile = open(fileName, "wb")
    pickle.dump(dataObject, outputFile)
    outputFile.close()

def readPickle(fileName):
    inputFile = open(fileName, "rb")
    dataObject = pickle.load(inputFile)
    inputFile.close()

    print("dataObject=" + str(dataObject))

def pickleIO():
    fileName = "pickle.bin"
    writePickle(fileName)
    readPickle(fileName)

if __name__ == "__main__":
    pickleIO()