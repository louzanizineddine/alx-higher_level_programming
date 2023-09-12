#!/usr/bin/python3
"""JSON TO STRING MODULE HAS ONE FUNCTION to_json_string"""

import json


def to_json_string(my_obj):
    """stringify the oject into a string no tests are needed"""
    return json.dumps(my_obj)
