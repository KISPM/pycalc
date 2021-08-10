#!/usr/bin/python3
# Not fancy, built for KISPM testing
import sys

if (len(sys.argv) == 4):
    if (sys.argv[1] == "add"):
        print(str(int(sys.argv[2]) + int(sys.argv[3])))
    elif (sys.argv[1] == "sub"):
        print(str(int(sys.argv[2]) - int(sys.argv[3])))
else:
    print("Error: expected 3 arguments, got " + str(int(len(sys.argv)) -1))