# A file contains a word 'Donkey' multiple times. You need to write a program which replaces the word with '$%&*^' by updating it.

with open('sample.txt') as f:
    content = f.read()

content = content.replace('Donkey', '$%&*^')

with open('sample.txt', 'w') as f:
    f.write(content)
