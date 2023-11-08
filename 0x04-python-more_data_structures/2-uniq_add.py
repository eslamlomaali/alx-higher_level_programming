#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    addd = 0
    for i in my_list:
        if i not in new:
            addd += i
            new.append(i)
    return addd
