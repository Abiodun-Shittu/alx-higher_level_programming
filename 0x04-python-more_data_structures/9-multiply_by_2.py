#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {n: a_dictionary[n] * 2 for n in a_dictionary}
    return new_dict
