#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line """


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line"""
    t = ""
    with open(filename) as fille:
        for l in fille:
            t += l
            if search_string in l:
                t += new_string
    with open(filename, "w") as fille2:
        fille2.write(text)
