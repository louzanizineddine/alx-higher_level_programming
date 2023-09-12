#!/usr/bin/python3

"""READ FILE MODULE HAS ONE FUNCTION read_file"""


def read_file(filename=""):
    """reads a file from disk and prints it"""
    with open(filename, "r") as f:
        for line in f:
            print(line)
