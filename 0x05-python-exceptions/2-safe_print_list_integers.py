#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    item = 0
    n = 0
    for k in my_list:
        try:
            if (item >= x):
                break
            print("{:d}".format(k), end="")
            item += 1
        except (ValueError, TypeError):
            n += 1
    if (item+n < x):
        raise IndexError("list index out of range")
    print("".format())
    return item
