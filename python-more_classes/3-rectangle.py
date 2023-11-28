#!/usr/bin/python3
"""this module will provide more insight about the notion of classes"""


class Rectangle:
    """class defining a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor method to initialize instances"""
        self.width = width
        self.height = height

    def __str__(self):
        """printing the symbol '#' with the H-W parameters"""
        for i in range(self.__height):
            for _ in range(self.__width):
                print('#', end='')
            if i != (self.__height - 1):
                print()
        return ""

    @property
    def width(self):
        """getter width method"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width method"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter height method"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter height method"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """function returning the area of the instance"""
        return self.__width * self.__height

    def perimeter(self):
        """funciton returning the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return self.__width * 2 + self.__height * 2
