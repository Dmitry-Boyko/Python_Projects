# http://www.learnpython.org/en/Loops
# for loop
numbers = [2, 3, 5, 7]
for number in numbers:
    print number

# Print out the numbers from 0 to 6
print '\n'
for x in range(5):
    print x
    
# Print out 3, 4, 5
print '\n'
for x in range(3, 6):
    print x
    
# Print out 3, 5, 7
print '\n'
for x in range(3, 8, 2):
    print x
    
# "While" loops
# Print out numbers from 0 to 4
print '\n'
count = 0
while count < 5:
    print count
    count += 1 # This is the same: count = count + 1

# "break" and "continue" statements
# Print out numbers from 0 to 4
print '\n'
print 'Print out numbers from 0 to 4, use "break" statement'
count = 0
while True:
    print count
    count += 1
    if count >= 5:
        break

# Print out only odd numbers - 1, 3, 5, 7, 9
print '\n'
print 'Print out only odd numbers - 1, 3, 5, 7, 9'
for x in range(10):
    #Check if x is "even"
    if x % 2 == 0:
        continue
    print x