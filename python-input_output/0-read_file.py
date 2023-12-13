#!/usr/bin/python3
"""asd"""


def read_file(filename=""):
    """asd"""
    with open(filename, 'r', encoding="utf-8") as f:
        content = f.read()
        print(content.strip(), end='')
