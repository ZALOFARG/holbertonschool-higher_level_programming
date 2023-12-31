#!/usr/bin/python3

"""write_file function"""


def write_file(filename="", text=""):
    """Write text into the file received as argument.

    Args:
        filename (file): File to write.
        text (str): Text to write into the file. Defualts (empty string).

    Returns:
        int: Number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
