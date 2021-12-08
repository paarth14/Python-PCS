# Write a python program to input eight numbers from user and display all the unique numbers once.

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))
num6 = int(input("Enter a number: "))
num7 = int(input("Enter a number: "))
num8 = int(input("Enter a number: "))

set1 = set()

set1.add(num1)
set1.add(num2)
set1.add(num3)
set1.add(num4)
set1.add(num5)
set1.add(num6)
set1.add(num7)
set1.add(num8)

print(set1)

# OUTPUT :-
# Enter a number: 1
# Enter a number: 22
# Enter a number: 3
# Enter a number: 22
# Enter a number: 1
# Enter a number: 5
# Enter a number: 6
# Enter a number: 7
# {1, 3, 5, 6, 7, 22}
