# Write a python program using function to find the greatest of three numbers.

def greatest_of_three(num1, num2, num3):
    if(num1 > num2 and num1 > num3):
        print(num1, "is largest")
    elif(num2 > num1 and num2 > num3):
        print(num2, "is largest")
    else:
        print(num3, "is largest")
        
greatest_of_three(int(input("Enter a positive integer: ")), 
int(input("Enter a positive integer: ")), 
int(input("Enter a Positive integer: ")))
