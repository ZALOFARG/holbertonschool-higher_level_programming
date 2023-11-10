#!/usr/bin/python3
def uppercase(str):
    for x in str:
        print(x if (ord(x) == 32) or (ord(x) in range(48, 58)) or (ord(x) in range(65, 91)) else (chr(ord(x) - 32)), end="")
    print()
