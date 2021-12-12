# Create a Multiplication table by taking a number and range input from the user.

num = int(input("Enter a positive integer: "))
range_mul = int(input("Enter the range of multiplication table: "))

for i in range(1, range_mul):
    print(num, " x ", i, " = ", num*i)
