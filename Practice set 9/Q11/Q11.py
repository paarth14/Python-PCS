# Write a python program to rename a file and delete the old file.

import os

oldname = 'sample2.txt'
newname = 'rename.txt'

with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)
    
os.remove(oldname)
