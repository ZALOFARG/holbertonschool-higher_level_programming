#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0:
        return None
    else:
        return my_list[idx]


if __name__ == '__main__':
    element_at(my_list, idx)
