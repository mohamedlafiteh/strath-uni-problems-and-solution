#!/usr/bin/env python3

import csv

def writeCSV(fileName):
    csvFile = open(fileName, "w", newline='')
    csvWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)

    dataTable = {}
    dataTable["Host name"] = ["localhost", "GoogleDNS"]
    dataTable["IP address"] = ["127.0.0.1", "8.8.8.8"]
    columnNames = list(dataTable.keys())

    csvWriter.writerow(columnNames)

    nRows = len(dataTable[columnNames[0]])

    for i in range(nRows):
        row = []
        for columnName in columnNames:
            row += [ dataTable[columnName][i] ] 
        csvWriter.writerow(row)
    csvFile.close()

def readCSV(fileName):
    csvFile = open(fileName, "r", newline='')
    csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')

    dataTable = {}
    columnNames = []
    numberOfColumns = 0
    for row in csvReader:
        if len(columnNames) == 0:
            columnNames += row
            numberOfColumns = len(columnNames)
            for columnName in row:
                dataTable[columnName] = []
            continue
        
        for i in range(numberOfColumns):
            if i >= len(row):
                break
            dataTable[columnNames[i]] += [ row[i] ] 

    csvFile.close()

    print("dataTable=" + str(dataTable))

def csvIO():
    fileName = "data.csv"
    writeCSV(fileName)
    readCSV(fileName)

if __name__ == "__main__":
    csvIO()