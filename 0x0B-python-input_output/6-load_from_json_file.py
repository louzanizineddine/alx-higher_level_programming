#!/usr/bin/python3
"""READ JSON FROM FILE MODULE HAS ONE FUNCTION load_from_json_file"""

import json


def load_from_json_file(filename):
    """load the oject from a json file"""

    with open(filename, 'r') as f:
        return json.loads(f.read())
