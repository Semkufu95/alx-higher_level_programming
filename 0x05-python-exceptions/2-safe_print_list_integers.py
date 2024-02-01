#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    item = 0
    n = 0
    for n in range(x)
        try:
            print('{:d}'.format(my_list[n]), end='')
            item += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
        print()
        return item
