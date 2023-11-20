#!/usr/bin/python3
"""This module will manage classes"""


class Square:
    """Creates and defines a class.

    do <obj> = class()
    get and instance of the class.
    """
    def __init__(self, size):
        """construct method

        Args:
            self: the object is being created.
            size: size of the square being created
        """
        self.__size = size
    pass
