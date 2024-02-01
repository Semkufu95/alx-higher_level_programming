#!/usr/bin/python3

def safe_print_list(my_list = [], x = 0):
    item = 0
    for n in range(x):
        print(my_list[n], end=' ')
        item += 1
    except IndexError:
        pass
    print()
    return item
