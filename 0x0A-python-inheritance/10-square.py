#!/usr/bin/python3
'''
A module for rectangle
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' A class that inherits from rectangle'''
    def __init__(self, size):
        '''Initialize the size'''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
