#!/usr/bin/python3
def max_integer(my_list=[]):
    ma_x = my_list[0]
    if not my_list:
        return None
    for i in my_list:
        if i > ma_x:
            ma_x = i
            return ma_x
