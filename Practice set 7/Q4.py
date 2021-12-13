# Write a Python Program to check whether a number is Prime or not.

num = int(input("Enter a positive integer: "))
flag = True

for i in range(2, num):
    if (num%i==0):
        flag = False
        break

if flag:
    print("Prime Number")
else:
    print("Not an Prime Number")
