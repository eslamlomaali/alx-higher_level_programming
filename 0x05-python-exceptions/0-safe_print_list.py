#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    result = 0
    for z in range(x):
        try:
            print(f"{my_list[z]}", end="")
            result += 1
        except IndexError:
            break
    print()
    return(result)
