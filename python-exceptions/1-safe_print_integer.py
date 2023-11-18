#!/usr/bin/python3
def safe_print_integer(value):
    if value is True or value is False:
        return 0
    else:
        try:
            print("{:d}". format(value))
            return True
        except ValueError:
            return 0


if __name__ == '__main__':
    safe_print_integer(value)
