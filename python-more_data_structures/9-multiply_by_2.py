#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b = a_dictionary.copy()
    for i in list(b.keys()):
        b[i] *= 2
    return b


if __name__ == '__main__':
    multiply_by_2(a_dictionary)
