# create multiple files

list1 = ['a', 'b', 'c']

for i in range(len(list1)):
    open('file%s.txt' % i, 'w').write(list1[i])
