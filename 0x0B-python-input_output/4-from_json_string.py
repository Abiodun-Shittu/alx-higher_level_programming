#!/usr/bin/python3
''' function that returns a python object represented by a JSON string
'''

import json


def from_json_string(my_str):
    ''' module from_json_string
     returns Python objects
    '''
    return json.loads(my_str)
