#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    a = 0
    b = 0
    for li in my_list:
        a += li[0] * li[1]
        b += li[1]
    return float(a / b)
