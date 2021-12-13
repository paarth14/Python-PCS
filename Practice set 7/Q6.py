# Write a python program to find factorial of a number.

num = int(input("Enter a positive integer: "))
fact = 1

for i in range(1, num+1):
    fact *= i
    
print("Factorial is: ", fact)
