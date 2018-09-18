
def my_max(lst):
    max_val = lst[0]       # initialize with the first value from the list
    for item in lst:       # loop over the items in the list
        if item > max_val: # compare current item with the maximum seen so far
            max_val = item # set new max
    return max_val         # return the max

lst = [1, 3, 6, 3, 8, 9, 73, 0]
max_val = lst[0]            # initialize with the first value from the list
for item in lst:            # loop over the items in the list
    if item > max_val:      # compare current item with the maximum seen so far
        max_val = item      # set new max
print max_val               # return the max