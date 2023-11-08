#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for intt in range(len(my_list)):
        if my_list[intt] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[intt])
    return new_list
