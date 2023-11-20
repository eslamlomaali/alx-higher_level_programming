#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    loop1 = []
    loop2 = 0
    if list_length <= 0:
        print("out of range")
        return loop1
    while loop2 < list_length:
        try:
            loop1.append(my_list_1[loop2] / my_list_2[loop2])
        except ZeroDivisionError:
            print("division by 0")
            loop1.append(0)
        except TypeError:
            print("wrong type")
            loop1.append(0)
        except IndexError:
            print("out of range")
            loop1.append(0)
        finally:
            loop2 += 1
    return loop1
