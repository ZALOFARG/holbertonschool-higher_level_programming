#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments.".format(len(argv) - 1))


if __name__ == '__main__':
    main()
