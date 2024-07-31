#!/usr/bin/python3
for i in range(0, 9):
    for j in range(i+1, 10):
        middle = ', '
        if i == 8:
            middle = '\n'
        print("{:d}{:d}".format(i, j), end=middle)
