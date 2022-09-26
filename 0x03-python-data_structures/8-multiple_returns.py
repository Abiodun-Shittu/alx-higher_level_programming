#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        first_char = None
        _tuple = (length, first_char)
        return _tuple
    else:
        first_char = sentence[0]
        _tuple = (length, first_char)
        return _tuple
