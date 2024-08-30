#!/usr/bin/python3
'''
Class MyInt
'''


class MyInt(int):
    '''class MyInt'''
    def __eq__(self, value):
        '''Override == to !='''
        return self.real != value

    def __ne__(self, value):
        '''Override != to =='''
        return self.real == value
