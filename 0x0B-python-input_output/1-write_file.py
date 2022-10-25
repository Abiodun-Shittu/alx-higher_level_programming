#!/usr/bin/python3
"""
function that write a string to text (UTF8) & return total of character written
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
