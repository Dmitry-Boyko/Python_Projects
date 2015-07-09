# From book "Dive into Python"

import sys

saveout = sys.stdout                                     
fsock = open('out.txt', 'w')                             
sys.stdout = fsock                                       
print 'This message will be logged instead of displayed' 
sys.stdout = saveout                                     
fsock.close()  
sys.stdout.close()

# ==========================

# And simple huck redirect loging 'print' to a file.

import sys

sys.stdout = open("file.txt", 'w')
print('foo')
sys.stdout.close()
