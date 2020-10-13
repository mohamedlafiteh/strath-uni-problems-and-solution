import csv
import json

"""
Load JSON into memory.
"""
def loadData(fileName, rows):
    del rows[:]
    inputFile = open(fileName, "r")
    rows += json.load(inputFile)
    inputFile.close()

"""
Find maxima and minima for input data.
"""
def findsMaxAndMin(rows, dataPoints):
    numberOfRows = len(rows)

    lastPosition = 0
    previousLast = 0
    gradientSign = 0

    for i in range(numberOfRows):
        if i == 0:
            lastPosition = rows[i]["distance"]
            continue
        if i == 1:
            previousLast = lastPosition
            lastPosition = rows[i]["distance"]
            continue

        # Find the gradient sign.
        if lastPosition > previousLast:
            gradientSign = 1
        if lastPosition < previousLast:
            gradientSign = -1
  
        currentPosition = rows[i]["distance"]
        if gradientSign > 0 and lastPosition > currentPosition:
            dataPoints["TimeStamp"] += [ rows[i-1]["time"] ]
            dataPoints["Distance"] += [ rows[i-1]["distance"] ]
            dataPoints["InflectionType"] += [ "Maximum" ]
        elif gradientSign < 0 and lastPosition < currentPosition:
            dataPoints["TimeStamp"] += [ rows[i-1]["time"] ]
            dataPoints["Distance"] += [ rows[i-1]["distance"] ]
            dataPoints["InflectionType"] += [ "Minimum" ]

        previousLast = lastPosition
        lastPosition = currentPosition

"""
A function to export data to CSV.
"""
def exportData(fileName, dataPoints):

    # Open output CSV file.
    outputFile = open(fileName, "w")
    csvWriter = csv.writer(outputFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    
    # Write the column headings.
    columnNames = list(dataPoints.keys())
    csvWriter.writerow(columnNames)

    # Write the data columns.
    numberOfRows = len(dataPoints[columnNames[0]])
    for i in range(numberOfRows):
        outputRow = []
        for columnName in columnNames:
            outputRow += [ dataPoints[columnName][i] ]
        
        csvWriter.writerow(outputRow)

    outputFile.close()

if __name__ == "__main__":
    rows = []
    loadData("mooninfo_2020.json", rows)

    dataPoints = {}
    dataPoints["TimeStamp"] = []
    dataPoints["InflectionType"] = []
    dataPoints["Distance"] = []

    findsMaxAndMin(rows, dataPoints)

    exportData("maxAndMin.csv", dataPoints)