#!/usr/bin/python3
"""this module will define a class then work with it"""


class BaseGeometry:
    """working with a class"""
    def area(self):
        """method that raises an excep"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """func that verifies value argument"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value
