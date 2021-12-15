# Write a Python program to convert inches to cms using function.

def convert_inches_to_cms(inches):
    formula = inches * 2.54
    print(formula, "cm")

convert_inches_to_cms(int(input("Enter inches: ")))
