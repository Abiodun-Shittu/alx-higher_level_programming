#!/usr/bin/python3
def remove_char_at(str, n):
    if 0 <= n < len(str):
        return (str.replace(str[n], ""))
    else:
        return (str)
