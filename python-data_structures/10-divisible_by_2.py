#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    lista = []

    for number in my_list:
        if number % 2 == 0:
            lista.append(True)
        else:
            lista.append(False)

    return lista
