#!/usr/bin/python3
import json
"""STRING TO JSON MODULE HAS ONE FUNCTION from_json_string"""


def from_json_string(my_str):
    """stringify the oject into a string"""
    return json.loads(my_str)
