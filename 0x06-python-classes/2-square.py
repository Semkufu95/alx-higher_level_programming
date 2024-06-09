#!/usr/bin/python3

'''import module or define the class'''


class Square:
    def __init__(self, size=0):
        ''' Initialize a new square '''
        if  not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif (size < 0):
            raise ValueError('size must be >= 0')
        self.__size = size
