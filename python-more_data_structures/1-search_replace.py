#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_copy = my_list.copy()
    index_list = []
    for i in range(len(list_copy)):
        if list_copy[i] == search:
            index_list.append(i)
    itera = list_copy.count(search)
    for j in range(itera):
        list_copy.remove(search)
    for k in index_list:
        list_copy.insert(k, replace)
    return list_copy


if __name__ == '__main__':
    search_replace(my_list, search, replace)
