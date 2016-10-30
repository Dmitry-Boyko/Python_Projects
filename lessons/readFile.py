print'week 7\n'
fhand = open('someName', 'r')
# or with open('someName', 'r') as fhand
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startwith('From'):
        count = count + 1
        print line
    print 'The were', count, 'subject lines in' ,fhand

fname = rawinput('Enter the file name')
try:
    fhand = open(fname)
except:
    print 'FIle cannot be opened', fname
    exit()
count = 0
for line in fhand:
    if line.startwith('Subject:'):
        count = count + 1
print 'The were', count, 'subject lines in' ,fhand
