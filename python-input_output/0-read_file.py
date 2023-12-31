#!/usr/bin/python3
"""this module will handle I/O in terms of opening, writting and closing files"""


def read_file(filename=""):
    """func that reads a file
    Args:
    filename: object to be read

    Returns:
    None
    """
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")


if __name__ == '__main__':
    read_file(filename="")
