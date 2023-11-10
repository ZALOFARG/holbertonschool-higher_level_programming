#!/usr/bin/python3
for i in range(1, 100):
    izq = i // 10
    der = i % 10
    if (izq != der) and der > izq:
        if i == 89:
            print("{:02}".format(i), end="")
        else:
            print("{:02}, ".format(i), end="")
print()
