#!/usr/bin/python3
"""Defines a class function for checking"""


def is_same_class(obj, a_class)
    """Check if an object is exactly instance.
    Args:
        obj (any): The object that will check.
        a_class (type): The class to match the type of obj to.
    Returns:
        True - If obj is exactly an instance of a_class
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
