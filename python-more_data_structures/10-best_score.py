#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        return max(a_dictionary, key=a_dictionary.get)


if __name__ == '__main__':
    best_score(a_dictionary)
