#!/usr/bin/python3
'''
A class MyList that inherits frim list
'''


class MyList(list):
'''A class that inherits from a list'''
    def print_sorted(self):
        print(sorted(self))
