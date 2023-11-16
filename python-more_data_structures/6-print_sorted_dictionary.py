#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}". format(k, v))


if __name__ == '__main__':
    print_sorted_dictionary(a_dictionary)
