#!/usr/bin/python3

'''Defines a class square '''


class Square:

    '''Represents a square'''

    def __init__(self, size=0):
        '''initiates the sizes of square'''
        self.size = size

    @property
    def size(self):
        ''' retrieves the size of square'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''sets size to a new value'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >=0')
        self.__size = value

    def area(self):
        ''' returns the area of square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''prints # on stdout'''
        for m in range(0, self.__size):
            [print('#', end='') for n in range(self.__size)]
            print('')
        if self.__size == 0:
            print('')
