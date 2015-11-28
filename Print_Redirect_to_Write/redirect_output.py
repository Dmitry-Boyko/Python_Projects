# From book "Dive into Python"
from __future__ import print_function  # should be top line of your code
import sys

saveout = sys.stdout                                     
fsock = open('out.log', 'w')                             
sys.stdout = fsock                                       
print 'This message will be logged instead of displayed' 
sys.stdout = saveout                                     
fsock.close()  
sys.stdout.close()

# ==========================

# And simple huck redirect loging 'print' to a file.
from __future__ import print_function  # should be top line of your code
import sys

sys.stdout = open("file.log", 'w')
print('foo')
sys.stdout.close()
