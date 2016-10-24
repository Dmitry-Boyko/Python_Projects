myList = [9, 13, 46, 23, 86, 43, 16]

def largeestNum(some_value):
    largest_so_far = -1
    print 'Before', largest_so_far
    
    for the_num in some_value:
        if the_num > largest_so_far:
            largest_so_far = the_num
        print largest_so_far, the_num
        
    print 'After', largest_so_far

def sumList(some_value):
    # Summing elements in the list by loop
    print 'Summing elements in the list by loop'
    zork = 0
    print 'Before', zork
    for thing in some_value:
        zork = zork + thing
        print zork, thing
    print 'After', zork

# Finding the Average in a Loop
def averg(some_value):
    print('Finding the Average in a Loop')
    count = 0
    sum = 0
    print 'Before', count, sum
    
    for value in some_value:
        count = count + 1
        sum  = sum + value
        print count, sum, value
    print 'After', count, sum, sum / count

def filteringLoop(some_value):
    print 'Before'
    for value in some_value:
        if value > 20:
            print 'Large number', value
    print 'Afrter'

largeestNum(myList)
sumList(myList)
averg(myList)
filteringLoop(myList)