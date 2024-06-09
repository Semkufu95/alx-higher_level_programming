#!/usr/bin/python3

'''Import module or define the class'''


class Square:
    ''' defines the type of class'''

    def __init__(self, size=0):
        '''Initiates the size of the class'''

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        ''' public instance method to return area'''
        return(self.__size ** self.__size)
