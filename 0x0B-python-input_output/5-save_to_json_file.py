#!/usr/bin/python3
"""SAVE TO JSON FILE MODULE HAS ONE FUNCTION to_json_string"""

import json


def save_to_json_file(my_obj, filename):
    """stringify the oject into a string no tests are needed"""
    json_obj = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(json_obj)
