#!/usr/bin/python
# -*- coding: utf-8 -*-
# weights calculator
#convert inch to centimeters
# 1 lb = 0.45359237 kg

def lb2kg():
    try:
        inpt = float(raw_input("type number of Labels and i will convert it to Kilograms: "))
        kg = inpt * 0.45359237
        print str(kg) + ' kg'
    except ValueError:
        print("That's not a number!")
