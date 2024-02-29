#!/usr/bin/python3
"""Write a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
        """Finds a peak in list_of_integers"""

        if list_of_integers is None or list_of_integers == []:
        return None
        lower = 0
        higher = len(list_of_integers)
        middle = ((higher - lower) // 2) + lower
        middle = int(middle)
        if higher == 1:
        return list_of_integers[0]
        if higher == 2:
        return max(list_of_integers)
        if list_of_integers[middle] >= list_of_integers[middle - 1] and\
        list_of_integers[middle] >= list_of_integers[middle + 1]:
        return list_of_integers[middle]
        if middle > 0 and list_of_integers[middle] < list_of_integers[middle + 1]:
        return find_peak(list_of_integers[middle:])
        if middle > 0 and list_of_integers[middle] < list_of_integers[middle - 1]:
            return find_peak(list_of_integers[:middle])
