#!/usr/bin/python3
'''
A module for rectangle
'''
BaseGeometry = __import__ ('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' A class that inherits from BaseGeometry'''
    def __init__(self, width, height):
        '''Initialize the width and height'''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
