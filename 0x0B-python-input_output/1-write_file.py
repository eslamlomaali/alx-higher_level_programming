#!/usr/bin/python3
"""function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """write content in UTF8 text file"""
    with open(filename, encoding="utf-8") as fille:
	fille.write("This School is so cool!\n")
