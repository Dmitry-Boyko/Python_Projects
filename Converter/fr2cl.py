#!/usr/bin/python
# -*- coding: utf-8 -*-
#convert Fahrenheit to Celsius formula  
# T(°C) = (T(°F) - 32) / 1.8

# C = 5/9 (F-32)

def fr2cl():
    try:
        inpt3 = float(raw_input("type temperature in Fahrenheits and i will convert it to Celsius: "))
        if inpt3 < -273.15:        
            return "That temperature doesn't make sense!" 
        else:
            inpt3 =  0.5555555555555 * (inpt3 - 32.0)
            print str(inpt3) + ' C'
    except ValueError:
        print("That's not a number!")
