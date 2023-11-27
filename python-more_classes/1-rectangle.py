#!/usr/bin/python3
"""this module will provide more insight about the notion of classes"""


class Rectangle:
    """class defining a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor method to initialize instances"""
        self.__width = width
        self.__height = height

    def width(self):
        """getter width method"""
        return self.__width

    def width(self, value):
        """setter width method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def height(self):
        """getter height method"""
        return self.__height

    def height(self, value):
        """setter height method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
