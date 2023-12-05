#!/usr/bin/python3
"""unction that writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file with JSON format"""
    with open(filename, "w") as fille:
        json.dump(my_obj, fille)
