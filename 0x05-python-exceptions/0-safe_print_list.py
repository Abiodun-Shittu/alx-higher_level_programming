#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            a += 1
    except IndexError:
        None
    print()
    return a
