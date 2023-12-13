#!/usr/bin/python3
"""this module will handle I/O in terms of opening, writting and closing files"""


def read_file(filename=""):
    """func that reads a file
    Args:
    filename: object to be read

    Returns:
    None
    """
    with open(filename, 'r', encoding="UTF8") as f:
        content = f.read()
        print(content.strip(), end='')


if __name__ == '__main__':
    read_file(filename="")
