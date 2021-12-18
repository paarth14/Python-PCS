# Write a Python Program to wipe out the contents of a file using python.

with open('wipe.txt') as f:
    f.read()

with open('wipe.txt', 'w') as f:
    f.write(" ")
