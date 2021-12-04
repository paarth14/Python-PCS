# Edit the below template using string functions.

# letter = '''Dear <|NAME|>,
# you are selected!
# <|DATE|>'''

letter = '''Dear <|NAME|>,
you are selected!
<|DATE|>'''
                   
name = input("Enter your name: ")
date = input("Enter the date: ")

letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)

print(letter)
