#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        finall = a / b
        print("Inside result: {:.1f}".format(finall))
    except:
        finall = None
        print("Inside result: {}".format(finall))
    finally:
        return finall
