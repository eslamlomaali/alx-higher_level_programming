#!/usr/bin/python3
"""Defines a functian ."""


def add_attribute(obj, att, value):
    """Add a new attribute
    Args:
        obj (any): The object add attribute to.
        att (str): The name of the attribute
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
