#!/usr/bin/python3
"""this module will handle I/O"""


def read_file(filename=""):
    """func that reads a file"""
    with open(filename, 'r', encoding="UTF8") as f:
        content = f.read()
        print(content.strip(), end='')


if __name__ == '__main__':
    read_file(filename="")
