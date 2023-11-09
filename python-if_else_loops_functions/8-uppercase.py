#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ((ord(x)) == 32) or (ord(x) in range(48, 58)):
            print(chr(ord(x)), end="")
        else:
            print(chr(ord(x) - 32), end="\n")
