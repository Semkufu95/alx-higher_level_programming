#!/usr/bin/python3
'''
Return True if an object is instance of class inherited
'''


def inherits_from(obj, a_class):
    ''' Check inheritance '''
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
