# Write a Python program to accept marks of 6 students and display them in a sorted manner.

student1 = int(input("Enter your marks: "))
student2 = int(input("Enter your marks: "))
student3 = int(input("Enter your marks: "))
student4 = int(input("Enter your marks: "))
student5 = int(input("Enter your marks: "))
student6 = int(input("Enter your marks: "))

list1 = [];

list1.append(student1)
list1.append(student2)
list1.append(student3)
list1.append(student4)
list1.append(student5)
list1.append(student6)

print("Unsorted list: ", list1)
list1.sort()
print("Sorted list: ", list1)
