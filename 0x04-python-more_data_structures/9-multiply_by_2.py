#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for by in a_dictionary:
        new[by] = a_dictionary[by] * 2
    return new
