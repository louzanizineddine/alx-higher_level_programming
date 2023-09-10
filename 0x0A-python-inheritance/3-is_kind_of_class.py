#!/usr/bin/python3
"""module that is_kind_of_class as function"""


def is_kind_of_class(obj, a_class):
    """ruturn true is obj is an instance of a_class or inherited"""
    return isinstance(obj, a_class)
