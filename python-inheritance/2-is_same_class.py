#!/usr/bin/python3
"""module working with a func"""


def is_same_class(obj, a_class):
    """verifies if an object is an instance of a class"""
    if type(obj) == a_class:
        return True
    else:
        return False


if __name__ == '__main__':
    is_same_class(obj, a_class)
