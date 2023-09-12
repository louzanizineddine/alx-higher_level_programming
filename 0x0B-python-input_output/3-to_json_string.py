#!/usr/bin/python3
import json
"""JSON TO STRING MODULE HAS ONE FUNCTION to_json_string"""


def to_json_string(my_obj):
    """stringify the oject into a string"""
    return json.dumps(my_obj)
