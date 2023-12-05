#!/usr/bin/python3
"""a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as f:
        for l in f:
            text += l
            if search_string in l:
                text += new_string
    with open(filename, "w") as ff:
        ff.write(text)
