#!/usr/bin/python
# -*- coding: utf-8 -*-
# weights calculator
#convert inch and pounds to centimeters and kilograms
 
# 1 Inch = 2.54 Centimeters

def inch2cm():
    try:
        inpt1 = float(raw_input("type number of inch and i will convert it to centimeters: "))
        cm = inpt1 * 2.54
        print str(cm) + ' cm'
    except ValueError:
        print("That's not a number!")
