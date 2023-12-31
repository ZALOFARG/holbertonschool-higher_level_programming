#!/usr/bin/python3

"""Returns the dictionary description of an instance of Class."""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure.

        Args:
            obj: An instance of a class with serializable attributes.

        Returns:
            dict: A dictionary describing the serialized object.
    """
    return obj.__dict__
