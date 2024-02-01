#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    item = 0
    n = 0
    try:
        for n in range(0, x):
            print("{}".format(my_list[n]), end='')
            item += 1
    except IndexError:
        pass
    print()
    return item
