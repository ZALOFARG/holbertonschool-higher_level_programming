#!/usr/bin/python3

"""text_indentation function"""


def text_indentation(text):
    """Prints a text with 2 new lines after each
    of these characters: '.', '?', ':' .

    Parameters:
        text (str): text to be printed

    Raises:
        TypeError: If text if not string type
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuations:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip(), end="")
