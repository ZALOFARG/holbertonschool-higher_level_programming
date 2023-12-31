#!/usr/bin/python3

def no_c(my_string):

    new_string = ""

    for char in my_string:

        word_ascii = ord(char)

        if word_ascii != 99 and word_ascii != 67:
            new_string += char

    return new_string
