#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value, int) and not isinstance(value, bool):
            print("{:d}".format(int(value)))
            return True
        else:
            raise Exception
    except:
        return False


if __name__ == '__main__':
    safe_print_integer(value)
