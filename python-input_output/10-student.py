#!/usr/bin/python3
"""moduel that work with classes"""

class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initialize a new instance

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            age (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict

        Args:
            attrs: something to be retrieved
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            value = self.__dict__.get(attr)
            if value is not None:
                result[attr] = value

        return result
