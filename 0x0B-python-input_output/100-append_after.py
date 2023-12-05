#!/usr/bin/python3
"""defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line
    """
    t = ""
    with open(filename) as f:
        for l in f:
            t += l
            if search_string in l:
                t += new_string
    with open(filename, "w") as ff:
        ff.write(t)
