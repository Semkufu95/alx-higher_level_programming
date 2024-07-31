#!/usr/bin/python3
"""
check if current character index is equal to length
"I" can be subtracted from "V" and "X",
"X" can be subtracted from "L" and "C",
"C" can be subtracted from "D" and "M".
However, "V", "L", and "D" cannot be used to represent subtraction.
"""
def roman_to_int(roman_string):
    total = 0
    num = 0
    if roman_string is not None:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
        listroman = list(roman.keys())
        length = len(roman_string)
        for char in roman_string:
            # print("++ "+char)
            if char in roman:
                # print("+ "+char, roman[char])
                if char in 'IXC':
                    if num < length-1:
                        if listrom[num+1] in 'VXLCDM':
                            total = total + (roman[listroman[num+1]]-roman[char])
                total += roman[char]
            num += 1
    return total
