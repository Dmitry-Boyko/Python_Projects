import random

print("test 1")

# IP's min and max number
ip = ".".join(map(str, (random.randint(0, 255)  
# will generate 4 group of numbers "xxx.xxx.xxx.xxx"
                        for _ in range(4))))
print ip


# or
print("\ntest 2")

 # generated randomly 10 ip addresses
for x in xrange(1,10): 
    # IP address will begin ...
    ip = "170.12."  
    # IP's min and max number
    ip += ".".join(map(str, (random.randint(0, 255)  
    # will generate last two group of numbers "xxx.xxx"
    for _ in range(2))))          
print ip
