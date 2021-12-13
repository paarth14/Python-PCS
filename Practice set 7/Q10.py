# Write a python program to print multiplication table in reversed order.

num=int(input("Enter the number: "))
print("\n")
for i in range (10,0,-1):
  print(f"{num} * {i} = {num*i}")
