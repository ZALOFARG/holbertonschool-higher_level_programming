#!/usr/bin/python3
from sys import argv


resultado = 0
for i in range(1, len(argv)):
    resultado += int(argv[i])
print(resultado)
