#!/usr/bin/python3
"""defines a text file-reading function"""


def read_file(filename=""):
    """print  UTF8 text file content"""
    with open(filename, encoding="utf-8") as fille:
        print(fille.read(), end="")
