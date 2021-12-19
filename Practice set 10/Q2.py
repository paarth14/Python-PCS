# Write a class Calculator capable of finding Square, Cube and Square root of number taking input from user.

class Calculator:
    def __init__(self, num):
        self.number = num
        
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    
    def squareRoot(self):
        print(f"The square root of {self.number} is {self.number**0.5}")
        
a = Calculator(int(input("Enter a positive integer: ")))
a.square()
a.cube()
a.squareRoot()
