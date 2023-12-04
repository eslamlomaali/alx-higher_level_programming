#!/usr/bin/python3
''' module of inherits_from
'''


def inherits_from(obj, a_class):
    '''the object is an instance of a class
    obj: an object
    a_class: a class
    returns Nothing
    '''
    return type(obj) != a_class and isinstance(obj, a_class)
