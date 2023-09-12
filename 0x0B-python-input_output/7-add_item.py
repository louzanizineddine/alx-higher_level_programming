#!/usr/bin/python3

"""ADD ITEM MODULE HAS ONE FUNCTION """

import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

arguments = sys.argv[1:]
all_arguments = []
try:
    all_args = load_from_json_file("add_item.json")
except Exception as e:
    save_to_json_file([], "add_item.json")
all_arguments += (arguments)
save_to_json_file(all_arguments, "add_item.json")