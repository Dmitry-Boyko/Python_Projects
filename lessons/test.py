a = [3, 4, 5]
b = [i for i in a if i > 4]
print b
# Or:
b = filter(lambda x: x > 4, a)
print b
