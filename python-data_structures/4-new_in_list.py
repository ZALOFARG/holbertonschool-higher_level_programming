#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        copia = []
        copia = my_list.copy()
        copia.remove(my_list[idx])
        copia.insert(idx, element)
        return copia


if __name__ == '__main__':
    replace_in_list(my_list, idx, element)
