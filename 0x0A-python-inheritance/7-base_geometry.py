#!/usr/bin/python3
'''
An empty class
'''


class BaseGeometry:
    '''A class for base geometry '''
    def area(self):
        '''method for un implemented area'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name,  value):
        '''method for validating values'''
        if type(value) is not int:
           raise TypeError(name + ' must be an integer')
        if value <= 0:
           raise ValueError(name + ' must be greater than 0')
