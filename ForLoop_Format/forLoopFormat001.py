#1/usr/bin/python

for num in range(10, 20):       # to iterate between 10 and 20
    for i in range(2, num):     # to iterate on the factor of the numer
        if num%i == 0:          # to determinate first factor
            j = num/i           # to iterate fit second factor
            print '%d equal %d * %d' % (num, i ,j)
            break               # to move to the next number (the first FOR)
    else:
        print num, 'is a prime number'
        