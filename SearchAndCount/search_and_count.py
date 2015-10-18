"""
Looking(do match by name and extension) and count inside directory
"""

import os
from fnmatch import fnmatch

root = '//Users//dmitryboyko//Documents//'
extension = '*.py'
name = 'test.*'

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
