#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == True or value == False:
            raise TypeError
        else:
            print("{:d}". format(value))
            return True
    except TypeError:
        return False
    except ValueError:
        return False


if __name__ == '__main__':
    safe_print_integer(value)
