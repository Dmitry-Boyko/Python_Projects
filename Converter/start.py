#!/usr/bin/python
# -*- coding: utf-8 -*-
# weights calculator
#convert inch and pounds to centimeters and kilograms
 
# 1 Inch = 2.54 Centimeters
# 1 kilogram = pound/2.2046  or lb = kg*2.2046
 
 
# Clears the screen

import os
if os.name == "nt":
    os.system("cls") # cls for windows
else:
    os.system("clear")
# End clearing

from lb2kg import lb2kg
from inch2cm import inch2cm
from fr2cl import fr2cl
from fr2cl import c_to_f

print 'convert lb to kg press                  "l"'
print 'convert inch to cm press                "i"'
print 'convert Fahrenheit to Celsius press     "f"'
print 'convert Celsius to Fahrenheit press     "c"'

choice = str(raw_input('Enter the letter for the next step: '))

if choice == "i":
                 inch2cm()
elif choice == "l":
                 lb2kg()
elif choice == "f":
			   	 fr2cl()
elif choice == "c":
                c_to_f()
else:
    print "You chosed wrong character"
 
class sizes():
    def __init__(self):
        self.inpt = 0
        self.cm = 0
 
 
class weights():
    def __init__(self):
        self.inpt = 0
        self.kg = 0
        
class temperature():
	def __init__(self):
		self.inpt = 0
		self.c = 0
