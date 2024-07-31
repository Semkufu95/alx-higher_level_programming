#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_arr = []
    num = 0
    for k in range(0, list_length):
        try:
            num = my_list_1[k]/my_list_2[k]
        except ZeroDivisionError:
            print("division by 0")
            num = 0
        except TypeError:
            print("wrong type")
            num = 0
        except IndexError:
            print("out of range")
            num = 0
        finally:
            new_arr.append(num)
    return new_arr
