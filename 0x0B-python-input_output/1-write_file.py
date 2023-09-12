#!/usr/bin/python3

"""READ FILE MODULE HAS ONE FUNCTION write_file"""


def write_file(filename="", text=""):
    """write text string to file in the disk"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
