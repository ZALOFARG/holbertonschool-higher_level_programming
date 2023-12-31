#!/usr/bin/python3

"""Student class"""


class Student:
    """Defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        Args:
            attrs: If is a list of string must be retrieved.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            value = self.__dict__.get(attr)
            if value is not None:
                result[attr] = value

        return result

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json: A dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
