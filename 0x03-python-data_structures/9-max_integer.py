#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return "None"
    else:
        m = my_list[0]
        for z in range(len(my_list)):
            if my_list[z] > m:
                m = my_list[z]
        return m
