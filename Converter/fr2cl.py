#!/usr/bin/python
# -*- coding: utf-8 -*-
# weights calculator
#convert inch and pounds to centimeters and kilograms

# C = 5/9 (F-32)

def fr2cl():
    try:
        inpt3 = int(raw_input("type temperature in Fahrenheits and i will convert it to Celsius: "))
        c =  0.5555555555555 * (inpt3 - 32.0)
        print str(c) + 'C'
    except ValueError:
        print("That's not a number!")
