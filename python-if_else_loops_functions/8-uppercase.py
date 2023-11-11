#!/usr/bin/python3
def uppercase(str):
    for x in str:
        print("{}".format(x) if ord(x) in range(32, 91) else "{}".format((chr(ord(x) - 32))), end="")
    print()
