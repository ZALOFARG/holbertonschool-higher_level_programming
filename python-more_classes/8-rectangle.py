#!/usr/bin/python3
"""this module will provide more insight about the notion of classes"""


class Rectangle:
    """class defining a rectangle"""
    number_of_instances = 0
    print_symbol = '#'
    def __init__(self, width=0, height=0):
        """constructor method to initialize instances"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __del__(self):
        print("Bye rectangle...")
        self.__class__.number_of_instances -= 1

    def __str__(self):
        """printing the symbol '#' with the H-W parameters"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for i in range(self.__height):
                for _ in range(self.__width):
                    print(self.__class__.print_symbol, end='')
                if i != (self.__height - 1):
                    print()
            return ""

    def __repr__(self):
        """repr method to get the formal description of the object"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"

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
    
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.__width * rect_1.__height >= rect_2.__width * rect_2.__height:
            return rect_1
        else:
            return rect_2
