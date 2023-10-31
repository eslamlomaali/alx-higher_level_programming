#!/usr/bin/python3
def remove_char_at(str, n):
    y = ""
    for z in range(len(str)):
        if z != n:
            y = y + str[z]
    return (y)
