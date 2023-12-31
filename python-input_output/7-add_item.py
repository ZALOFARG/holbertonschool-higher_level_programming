#!/usr/bin/python3
"""A script that adds all arguments to a Python list, and then save them to a file."""

from sys import argv
from os.path import exists
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

# Check if the file exists, load its content if it does
if exists(filename):
    py_list = load_from_json_file(filename)
else:
    py_list = []


# Add command line arguments to the list
py_list.extend(argv[1:])

# Save the updated list to the file
save_to_json_file(py_list, filename)
