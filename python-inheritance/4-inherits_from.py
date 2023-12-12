#!/usr/bin/python3
"""In this module we'll work with inheritance"""


def inherits_from(obj, a_class):
    """func that verifies if an instance is a subclass of a superclass"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False


if __name__ == '__main__':
    inherits_from(obj, a_class)
