#!/usr/bin/python3
"""STRING TO JSON MODULE HAS ONE FUNCTION from_json_string"""

import json


def from_json_string(my_str):
    """stringify the oject into a string no test are needed"""
    return json.loads(my_str)
