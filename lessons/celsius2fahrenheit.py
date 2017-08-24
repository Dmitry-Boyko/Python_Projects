
print('ex 01')

def c2f(cels):
    tf = tc * 1.8 + 32
    return tf
    
tc = input("Please add Temperature in Celsius: ")

print(c2f(tc))

print('\nex 02')
money={"saving_account":200, "checking_account":100, "under_bed":[500,10,100]}
print(money['under_bed'][1])