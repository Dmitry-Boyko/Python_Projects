#!/usr/bin/python
# -*- coding: utf-8 -*-
#convert Fahrenheit to Celsius formula  
# T(°C) = (T(°F) - 32) / 1.8

# C = 5/9 (F-32)

def fr2cl():
    try:
        inpt = float(raw_input("type number Fahrentheit and i will convert it to Celsius: "))
        cl = 0.5555555555555 * (inpt - 32.0)
        print str(cl) + ' C'
    except ValueError:
        print("That's not a number!")


def c_to_f():    
    inpt = float(raw_input("type number Celsius and i will convert it to Fahrentheit: "))
    if inpt < -273.15:        
        return "That temperature doesn't make sense!"    
    else:        
        f = inpt * 9 / 5 + 32        
        #return f
        print str(f) + ' F'
    #print(c_to_f(-273.4))