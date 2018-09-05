"""
1. expect user input
2. use if method for selection
Odd = 1,3,,7,...
Even = 2, 4, ... 8, ...
"""

num = float(raw_input("please enter some number:>  "))
if (num % 2) == 0:
    #print("The number", num, "is Even")
    print("{0} is Even".format(num))
else:
    #print("The number", num, "is Odd")
    print("{0} is Odd".format(num))