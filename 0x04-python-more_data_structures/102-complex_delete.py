#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for i in list(a_dictionary.keys()):
        if a_dictionary[i] == value:
            a_dictionary.pop(i, None)
    return a_dictionary
