#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
residuo = number % 10
if residuo == 0:
    print("Last digit of", number, "is", residuo, "and is 0")
elif residuo < 6 and residuo != 0:
    print("Last digit of", number, "is", residuo, "and is less than 6 and not 0")
else:
    print("Last digit of", number, "is", residuo, "and is greater than 5")
