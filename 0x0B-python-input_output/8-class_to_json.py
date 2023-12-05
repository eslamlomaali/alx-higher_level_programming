#!/usr/bin/python3
""" function returns the dictionary description with simple data structure"""


def class_to_json(obj):
    """Returns the dictionary model for a simple data structure"""
    return obj.__dict__
