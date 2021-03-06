"""
"fnmatch" module compares file names against glob-style patterns such as used by Unix shells.
Find more information: 
https://pymotw.com/2/fnmatch/
http://www.pythonforbeginners.com/fnmatch/os-walk-and-fnmatch-in-python
"""

import os
from fnmatch import fnmatch

root = '//Users//dmitryboyko//Documents//'
extension = 'test*.py'

counts = 0

for path, dirs, files in os.walk(root):
    for name in files:
        if fnmatch(name, extension):
            print(os.path, name)

            # count repeated files inside directory
            #num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
            #print(num_files)

            # count number of files
            counts += 1
            print(counts)
