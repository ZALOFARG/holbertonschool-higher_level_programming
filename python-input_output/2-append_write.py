#!/usr/bin/python3

"""append_write function"""


def append_write(filename="", text=""):
        """Write text into the file received as argument.

        Args:
            filename (file): File to append some text.
            text (str): Text to append into the file. Defualts (empty string).

        Returns:
            int: Number of characters added.
        """
        with open(filename, 'a', encoding="utf-8") as f:
            return f.write(text)
