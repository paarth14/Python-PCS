# Write a python program to mine a log file and find out whether it contains 'Python' or not ?

with open('log.txt') as f:
    content = f.read()

if 'Python' in content:
    print("It is Present")

else:
    print("It is not Present")
