#/usr/bin/python

for num in range(10, 20):       # to iterate between 10 and 20
    for i in range(2, num):     # to iterate on the factor of the numer
        if num%i == 0:          # to determinate first factor
            j = num/i           # to iterate fit second factor
            print '%d equal %d * %d' % (num, i ,j)
            break               # to move to the next number (the first FOR)
    else:
        print num, 'is a prime number'

print('\n')

password = ""
while password != "password123":
    password = raw_input("Enter you password: ")
    if password == "password123":
        print("You are logged in")
    else:
        print("Wrong input. Try again")

print("\n")

names = ['james', 'chris', 'stas']
email_domain = ['gmail', 'hotmail', 'yahoo']

for i, j in zip(names, email_domain):
    print(i, j)

print('\n')

temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c > -273.15:
        f=c*9/5+32
        return f
    else:
        return "That temperature doesn't make sense!"
for t in temperatures:
    print(c_to_f(t))
#If your version looked like below, that's still correct:
temperatures=[10,-20,-289,100]
def c_to_f(c):
    if c< -273.15:
        return "That temperature doesn't make sense!"
    else:
        f=c*9/5+32
        return f
for t in temperatures:
    print(c_to_f(t))