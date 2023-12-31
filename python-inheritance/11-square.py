#!/usr/bin/python3
"""this module will define a subclass of the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a inheriting sub-class"""
    def __init__(self, size):
        """Initialize validating size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Return the area"""
        return self.__size ** 2

    def __str__(self):
        """Returns an informal str repr of the instance"""
        return f"[Square] {self.__size}/{self.__size}"
