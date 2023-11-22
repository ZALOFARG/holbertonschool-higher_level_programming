#!/usr/bin/python3
"""This module will manage classes"""


class Square:
    """Creates and defines a class.

    do <obj> = class()
    get and instance of the class.
    """
    def __init__(self, size=0):
        """construct method

        Args:
            self: the object is being created.
            size: size of the square being created
        """
        self.size = size

    def area(self):
        """public method that returns the area of the square"""
        return self.__size ** 2
    def my_print(self):
        """public method that prints a square with dimension 'size' hatched with '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """getter configured in order to return the value"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter configured in order to replace a value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
