#!/usr/bin/python
# -*- coding: utf-8 -*-
# weights calculator
#convert inch to centimeters
# 1 lb = 0.45359237 kg

def lb2kg():
    try:
        inpt = int(raw_input("type number of inch and i will convert it to centimeters: "))
        kg = inpt * 0.45359237
        print str(kg) + ' kg'
    except ValueError:
        print("That's not a number!")
