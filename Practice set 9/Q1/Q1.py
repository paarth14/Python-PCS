# Write a Python Program to read the text from a given file 'poems.txt' and find out whether is contains the 'twinkle' or not.

f = open('poems.txt')
data = f.read()
if 'twinkle' in data:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()
