#!/usr/bin/python3

'''Defines a class square '''


class Square:

    '''Represents a square'''

    def __init__(self, size=0, position=(0, 0)):
        '''initiates the sizes of square'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
        
    def area(self):
        ''' returns the area of square'''
        return (self.__size * self.__size)

    def my_print(self):
        '''prints # on stdout'''

        if self.__size == 0:
            print('')
            return
        
        [print('') for m in range(0, self.__position[1])]
        for m in range(0, self.__size):
            [print(' ', end='') for n in range(0, self.__position[0])]
            [print('#', end='') for p in range(0, self.size)]
            print('')
