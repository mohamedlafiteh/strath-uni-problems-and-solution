#!/usr/bin/env python3

def buildTuple():
    return ("Database", "WebService", "Client")

if __name__ == "__main__":
    tupleValues = buildTuple() 

    print(tupleValues)
    print(tupleValues[1:3])