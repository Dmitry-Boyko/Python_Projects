import random

print("test 1")
ip = ".".join(map(str, (random.randint(0, 255)          # IP's min and max number
                        for _ in range(4))))            # will generate 4 group of numbers "xxx.xxx.xxx.xxx"
print ip


# or
print("\ntest 2")


for x in xrange(1,10):                                  # generated randomly 10 ip addresses
    ip = "170.12."                                      # IP address will begin ...
    ip += ".".join(map(str, (random.randint(0, 255)     # IP's min and max number
                          for _ in range(2))))          # will generate last two group of numbers "xxx.xxx"
    print ip
