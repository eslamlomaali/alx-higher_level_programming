#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        finall = a / b
         except (TypeError, ZeroDivisionError):
        finall = None
    finally:
        print("Inside result: {}".format(finall))
    return (finall)
