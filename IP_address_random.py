import random

ip = ".".join(map(str, (random.randint(0, 255)
                        for _ in range(4))))
