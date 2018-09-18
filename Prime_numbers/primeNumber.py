for num in range(2,101):    # to iterate between 10 to 20
    prime = True
    for i in range(2,num):  # to iterate on the factors of the number
        if (num%i==0):      # to determine the first factor
            prime = False
    if prime:
       print num
       
print "Another variation\n"       
#  You can write the same much shorter and more pythonic:

for num in range(2,101):
    if all(num%i!=0 for i in range(2,num)):
       print num

print "\nfrom user input\n"

number = int(raw_input("Pleae add some number here: > "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print number, "is not a prime number"
            break
        else:
            print "Yes", number, " is prime number!"
            break
else:
    print "something going wrong"