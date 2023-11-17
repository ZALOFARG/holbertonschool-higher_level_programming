#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}". format(value))
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    safe_print_integer(value)
