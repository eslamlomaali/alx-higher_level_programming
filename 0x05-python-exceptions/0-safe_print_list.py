#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
     loop = 0
    while True:
        try:
            if loop < x:
                print(my_list[loop], end='')
                loop += 1
            else:
                print()
                return loop
        except IndexError:
            print()
            return loop
