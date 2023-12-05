#!/usr/bin/python3
"""function that append a string to a text file (UTF8).."""


def append_write(filename="", text=""):
    """append content in UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as fille:
        return fille.write(text)
