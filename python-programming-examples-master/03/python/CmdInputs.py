#!/usr/bin/env python3

import getopt
import os
import sys

def usage(scriptName):
    print("Usage: " + scriptName + " [options]" + "\n")
    print("where [options] includes:")
    print("\t" + "-h, --help")
    print("\t" + "-o, --output <file name>" + "\n")

def main():
    print("argv=" + str(sys.argv))
    if len(sys.argv) == 1:
        return
    
    scriptName = os.path.basename(sys.argv[0])
    print("scriptName=\"" + scriptName + "\"")
    print()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        usage(scriptName)
        sys.exit(2)

    output = ""
    for option, value in opts:
        if option in ("-h", "--help"):
            usage(scriptName)
            sys.exit()
        elif option in ("-o", "--output"):
            output = value
        else:
            assert False, "unhandled option"

    print("output=\"" + output + "\"")


if __name__ == "__main__":
    main()