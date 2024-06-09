#!/usr/bin/python3

'''Import module or define the class'''


class Square:
    ''' defines a Square with four sizes'''

    def __init__(self, size=0):
        '''Initiates the size of the square'''
        self.size = size

    @property
    def size(self):
        ''' retrieves the size of square '''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''sets a new value of instance size'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''public instance to define area'''
        return (self.__size * self.__size)
