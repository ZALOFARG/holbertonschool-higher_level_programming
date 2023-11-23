#!/usr/bin/python3
"""This module two strings in one"""


def say_my_name(first_name, last_name=""):
    """
    this function evaluates the inputs and then concatenates

    Args:
        first_name: first sentence to be concatenated
        last_name: second sentence to be concatenated

    Returns: two strings concatenated in one
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == '__main__':
    say_my_name(first_name, last_name="")
