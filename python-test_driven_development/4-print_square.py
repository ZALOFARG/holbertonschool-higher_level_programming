#!/usr/bin/python3
"""This module will be used to print a square based on its parameter"""
def print_square(size):
    """
    print_square: function that prints to the stdout a square with dimension 'size'

    Args:
        size(int): linear dimension of the square

    Returns a square hatched with the pattern '#'
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and (size < 0):
        raise TypeError("size must be an integer")
    if size == 0:
        print()
    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()


if __name__ == '__main__':
    print_square(size)
