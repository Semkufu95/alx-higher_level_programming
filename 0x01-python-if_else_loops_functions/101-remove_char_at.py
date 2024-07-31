#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    for k in range(0, len(str)):
        if k == n:
            continue
        new_str += str[k]
    return new_str
