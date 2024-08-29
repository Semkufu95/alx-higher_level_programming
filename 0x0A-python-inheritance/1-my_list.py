#!/usr/bin/python3
'''
A class MyList that inherits from list
'''


class MyList(list):
    '''A class that inherits from a list'''
    def print_sorted(self):
        ''' Print a sorted list'''
        print(sorted(self))
