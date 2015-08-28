import random

ip = ".".join(map(str, (random.randint(0, 255)
                        for _ in range(4))))

# or

for x in xrange(1,100):
  ip = "170.12."
  ip += ".".join(map(str, (random.randint(0, 255) 
                          for _ in range(2))))
