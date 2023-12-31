#!/usr/bin/python3

"""Call the json module"""
import json

def to_json_string(my_obj):
        """Returns the JSON representation of an object.

            Args:
                my_obj (obj): Object to parse to JSON.

            Returns:
                JSON: JSON representation of my_obj.
        """
        return json.dumps(my_obj)
