#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    tuple_c = []
    veces_a = 2 - len(tuple_a)
    veces_b = 2 - len(tuple_b)
    if len(tuple_a) < 2:
        for i in range(veces_a + 1):
            tuple_a.append(0)
    if len(tuple_b) < 2:
        for i in range(veces_b + 1):
            tuple_b.append(0)
    for i in range(2):
        tuple_c.append(tuple_a[i] + tuple_b[i])
    tuple_c = tuple(tuple_c)
    return tuple_c


if __name__ == '__main__':
    add_tuple(tuple_a=(), tuple_b=())
