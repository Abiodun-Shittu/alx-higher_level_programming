#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for index in range(1, 3):
        try:
            if index > a:
                raise Exception('Too far')
            result += a ** b / index
        except Exception:
            result = b + a
            break
    return result
