#!/usr/bin/env python3

import datetime

def writeFile(fileName):
    outputFile = open(fileName, "w")
    outputFile.write("Data file" + "\n")
    outputFile.write("Date:" + str(datetime.datetime.utcnow()) + "\n")
    
    ipAddresses = []
    ipAddresses += [ "127.0.0.1" ]
    ipAddresses += [ "8.8.8.8" ]
    ipAddresses += [ "8.8.4.4" ]

    values = ""
    for ipAddress in ipAddresses:
        if len(values) == 0:
            values += ipAddress
        else:
            values += "\t" + ipAddress

    outputFile.write("Values:" + values + "\n")
    outputFile.close()

def readFile(fileName):
    inputFile = open(fileName, "r")
    allLines = inputFile.readlines()
    inputFile.close()

    dataRead = {}
    dataRead["Date"] = ""
    dataRead["Values"] = ""
    for line in allLines:
        line = line.strip()

        for key in dataRead.keys():
            if line.startswith(key + ":"):
                dataRead[key] = line[len(key)+1:]
                break
    
    print("dataRead=" + str(dataRead))
    values = dataRead["Values"].split("\t")
    print("values=" + str(values))

def fileIO():
    fileName = "fileIO.txt"
    writeFile(fileName)
    readFile(fileName)

if __name__ == "__main__":
    fileIO()