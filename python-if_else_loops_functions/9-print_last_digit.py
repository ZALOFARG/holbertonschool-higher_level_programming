#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number *= -1
        print(number % 10, end="")
    else:
        print(number % 10, end="")
    return number % 10


if __name__ == '__main__':
    print_last_digit()
