#!/usr/bin/python3
"""Module working with inheritance"""

class MyList(list):
    """defining a class tha tinherits from list"""
    def __init__(self):
        """constructor"""
        pass

    def print_sorted(self):
        """instance method that sorts out the list"""
        print(sorted(self))
