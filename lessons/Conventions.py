# Conventions
# Goood coding style

# Short Ways to Manipulate Lists
a = [3, 4, 5]
b = [i for i in a if i > 4]
print b
# Or:
b = filter(lambda x: x > 4, a)
print b

a = [3, 4, 5]
a = [i + 3 for i in a]
# Or:
a = map(lambda i: i + 3, a)

# Use enumerate() keep a count of your place in the list.
a = [3, 4, 5]
for i, item in enumerate(a):
    print i, item
# prints
# 0 3
# 1 4
# 2 5

# Or:
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
list(enumerate(seasons, start=1))
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# Equivalent to:
def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1

# Access a Dictionary Element
d = {'hello': 'world'}

print d.get('hello', 'default_value') # prints 'world'
print d.get('thingy', 'default_value') # prints 'default_value'

# Or:
if 'hello' in d:
    print d['hello']


# Read From a File
with open('file.txt') as f:
    for line in f:
        print line