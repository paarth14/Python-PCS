# Write a Python Program to create a multiplication of by taking number and range input from user by using functions.

def mul_table(n, range_n):
    for i in range(1,range_n+1):
        print(n, " * ", i, " = ", n*i)
        
mul_table(int(input("Enter a positive integer: ")), int(input("Enter the range of multiplication table: ")))
