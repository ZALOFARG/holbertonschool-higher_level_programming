#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0 and number != 0:
    number *= -1
    resto_neg = number % 10
    print("Last digit of", number * -1, "is", resto_neg * -1, "and is less than 6 and not 0")
else:
    resto = number % 10
    if resto == 0:
        print("Last digit of", number, "is", resto, "and is 0")
    if resto < 6 and resto != 0:
        print("Last digit of", number, "is", resto, "and is less than 6 and not 0")
    if resto > 5:
        print("Last digit of", number, "is", resto, "and is greater than 5")
