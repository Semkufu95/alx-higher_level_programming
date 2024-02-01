#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    item = 0
    n = 0
    try:
        for n in range(0, x):
            print('{:d}'.format(my_list[n]), end='')
            item += 1
            break
        except IndexError:
            continue
        print()
        return item
