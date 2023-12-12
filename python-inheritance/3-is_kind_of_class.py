#!/usr/bin/python3
"""this module will cover instances and sub-instances"""
def is_kind_of_class(obj, a_class):
    """func that verifies if an obj is an ins of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False


if __name__ == '__main__':
    is_kind_of_class(obj, a_class)
