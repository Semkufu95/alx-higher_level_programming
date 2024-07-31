#!/usr/bin/python3
def magic_calculation(a, b):
    jibu = 0
    for k in range(1, 3):
        try:
            if (k > a):
                raise Exception('Too far')
            else:
                jibu += (a ** b) / k
        except Exception:
            jibu = b + a
            break
    return (jibu)
