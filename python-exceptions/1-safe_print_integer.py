#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value == True or value == False:
            raise Exception
        else:
            print("{:d}". format(value))
            return True
    except Exception:
        return 0


if __name__ == '__main__':
    safe_print_integer(value)
