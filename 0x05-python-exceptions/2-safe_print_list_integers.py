#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    loop = loop2 = 0
    while True:
        try:
            if loop < x:
                print("{:d}".format(my_list[loop]), end='')
                loop += 1
                loop2 += 1
            else:
                print()
                return loop2
        except (ValueError, TypeError):
            loop += 1
