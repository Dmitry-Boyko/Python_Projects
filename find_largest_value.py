largest_so_far = -1
print 'Before', largest_so_far

for the_num in [9, 13, 46, 23, 86, 43, 16]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print largest_so_far, the_num
    
print 'After', largest_so_far

# Summing elements in the list by loop
print 'Summing elements in the list by loop'
zork = 0
print 'Before', zork
for thing in [9, 13, 46, 23, 86, 43, 16]:
    zork = zork + thing
    print zork, thing
print 'After', zork
