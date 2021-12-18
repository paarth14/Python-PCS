# Write a Python program to for a list of animals name that needs to be censored.

words = ['Dog', 'Elephant', 'Donkey', 'Buffalo']

with open('sample.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, '@#$%')

with open('sample.txt', 'w') as f:
    f.write(content)
    
