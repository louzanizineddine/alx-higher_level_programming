#!/user/bin/python3
"""
Module: object_inspector

Provides a function for inspecting Python object attributes and methods.

Usage:
    - Call `lookup(obj)` to get a list of attributes
    - and methods of the input object.
"""


def lookup(obj):
    """dir is a builtin function"""

    return dir(obj)
