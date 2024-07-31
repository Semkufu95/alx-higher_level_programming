#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for s in str:
        if 'a' <= s <= 'z':
            new_str+= chr((ord(s) - ord('a')) + ord('A'))
        else:
            new_str += s
    return new_str


for k in range(ord('z'), ord('a')+-1, -1):
    if k % 2 == 1:
        k = ord(uppercase(chr(k)))
    print("{}".format(chr(k)), end='')
