# Write a Python Program for the sum of first n numbers.

num = int(input("Enter a positive integer: "))

summ = 0
while(num>0):
    summ += num
    num -= 1
print("Sum is: ", summ)
