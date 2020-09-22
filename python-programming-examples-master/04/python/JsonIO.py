#!/usr/bin/env python3

import json

class DataSet():
    def __init__(self):
        self.name = ""
        self.dataSlices = []

    def __str__(self):
        stringValue = "{name=" + self.name
        stringValue += ",dataSlices=" + str(self.dataSlices) + "}"
        return stringValue

    def __repr__(self):
        return self.__str__()
    
    def toJson(self):
        dataSet = {}
        dataSet["name"] = self.name
        dataSet["dataSlices"] = []
        for dataSlice in self.dataSlices:
            dataSet["dataSlices"] += [ dataSlice.toJson() ]
        return dataSet

    def fromJson(self, jsonData):
        self.name = ""
        del self.dataSlices[:] 
        if "name" in jsonData.keys():
            self.name = jsonData["name"]
        if "dataSlices" in jsonData.keys():
            for dataSliceDef in jsonData["dataSlices"]:
                dataSlice = DataSlice()
                dataSlice.fromJson(dataSliceDef)
                self.dataSlices += [ dataSlice ]

class DataSlice():
    def __init__(self):
        self.name = ""
        self.dataTable = {}

    def __str__(self):
        stringValue = "{name=" + self.name
        stringValue += ",dataTable=" + str(self.dataTable) + "}"
        return stringValue

    def __repr__(self):
        return self.__str__()

    def toJson(self):
        dataSlice = {}
        dataSlice["name"] = self.name
        dataSlice["dataTable"] = self.dataTable.copy()
        return dataSlice

    def fromJson(self, jsonData):
        self.name = ""
        self.dataTable.clear() 
        if "name" in jsonData.keys():
            self.name = jsonData["name"]
        if "dataTable" in jsonData.keys():
            self.dataTable = jsonData["dataTable"].copy()

def writeJson(fileName):
    dataSet = DataSet()
    dataSet.name = "Input data"
    dataSet.dataSlices += [ DataSlice() ]
    dataSet.dataSlices += [ DataSlice() ]
    dataSet.dataSlices[0].name = "Training sample"
    dataSet.dataSlices[0].dataTable["x-axis"] = [ 1.0, 2.0, 3.0, 4.0, 5.0 ]
    dataSet.dataSlices[0].dataTable["y-axis"] = [ 11.0, 16.3, 12.1, 9.2, 4.2 ]
    dataSet.dataSlices[1].name = "Analysis data"
    dataSet.dataSlices[1].dataTable["x-axis"] = [ 1.0, 2.0, 3.0, 4.0, 5.0 ]
    dataSet.dataSlices[1].dataTable["y-axis"] = [ 13.0, 15.7, 10.4, 10.1, 3.9 ]
    jsonData = dataSet.toJson()

    outputFile = open(fileName, "w", encoding="utf-8")
    json.dump(jsonData, outputFile, ensure_ascii=False, indent=4)
    outputFile.close()

def readJson(fileName):
    inputFile = open(fileName, "r", encoding="utf-8")
    jsonData = json.load(inputFile)
    inputFile.close()

    dataSet = DataSet()
    dataSet.fromJson(jsonData)
    print(dataSet)

def jsonIO():
    fileName = "jsonData.json"
    writeJson(fileName)
    readJson(fileName)

if __name__ == "__main__":
    jsonIO()