#!/usr/bin/python3
"""function that returns an objec represented by a JSON string"""


import json


def from_json_string(my_str):
    """Returns the Python object model a JSON string"""
    return json.loads(my_str)
