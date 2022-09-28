#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dict = sorted(a_dictionary)
    for i in sorted_dict:
        print("{}: {}".format(i, a_dictionary[i]))
