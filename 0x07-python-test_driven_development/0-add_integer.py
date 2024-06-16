#!/usr/bin/python3

def add_integer(a, b=98):
    ''' 
    Adds two integers.
    Args:
         a (int or float): The first number
         b (int or float): The second number, defaults to 98
    Returns: sum of a and b
    '''

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')

    a = int(a)
    b = int(b)

    return a + b
