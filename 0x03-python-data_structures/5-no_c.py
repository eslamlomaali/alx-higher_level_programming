#!/usr/bin/python3
def no_c(my_string):
    S = my_string.translate({ord(z): None for z in 'cC'})
    return S
