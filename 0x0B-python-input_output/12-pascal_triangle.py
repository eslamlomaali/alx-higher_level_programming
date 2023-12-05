#!/usr/bin/python3
"""Create a function that returns a list of lists of integers"""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    trian = [[1]]
    while len(trian) != n:
        t = trian[-1]
        p = [1]
        for x in range(len(t) - 1):
            p.append(t[x] + t[x + 1])
        p.append(1)
        trian.append(p)
    return trian
