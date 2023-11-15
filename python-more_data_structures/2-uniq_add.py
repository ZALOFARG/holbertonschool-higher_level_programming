#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    my_list2 = list(my_set)
    suma = 0
    for i in my_list2:
        suma += i
    return suma


if __name__ == '__main__':
    uniq_add(my_list=[])
