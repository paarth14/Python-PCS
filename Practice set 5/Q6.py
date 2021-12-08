# Create an empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique.

favlang = {}

a = input("Enter your favourite language, Shubham: ")
b = input("Enter your favourite language, Ramesh: ")
c = input("Enter your favourite language, Suresh: ")
d = input("Enter your favourite language, Vansh: ")

favlang['Shubham'] = a
favlang['Ramesh'] = b
favlang['Suresh'] = c
favlang['Vansh'] = d

print(favlang)
