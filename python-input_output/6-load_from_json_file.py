#!/usr/bin/python3

"""Call the json module"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

     Args:
        filename (file): File in JSON representation.
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
