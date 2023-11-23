#!/usr/bin/python3
"""Module containing the different math expretions"""


def add_integer(a, b=98):
    """
    function that after validating the inputs returns a sum

    Args:
        a: operand 1
        b: operand 2

    Returns the sum
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 98
    return int(a + b)


if __name__ == '__main__':
    add_integer(a, b=98)
