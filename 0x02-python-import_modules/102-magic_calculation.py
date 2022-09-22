#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        sum = add(a, b)
        for i in range(4, 6):
            sum = add(sum, i)
        return sum
    else:
        return sub(a, b)
