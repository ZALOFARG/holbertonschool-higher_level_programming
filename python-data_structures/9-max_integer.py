#!/usr/bin/python3
def max_integer(my_list=[]):
    max_num = -9999
    if len(my_list) == 0:
        return None
    else:
        for i in range(len(my_list)):
            if my_list[i] > max_num:
                max_num = my_list[i]
        return max_num


if __name__ == '__main__':
    max_integer(my_list=[])
