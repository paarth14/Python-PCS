# Create a Calculator class and capable of finding square, square root, cube and greet the user without using the self argument.

class Calculator:
    def __init__(self, num):
        self.number = num
        
    def square(self):
        print(f"The sqaure of {self.number} is {self.number**2}")
    
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
        
    def squareRoot(self):
        print(f"The sqaureRoot of {self.number} is {self.number**0.5}")
    
    @staticmethod
    def greet():
        print("*******Hello there welcome to the best calculator of the world*******")
        
a = Calculator(int(input("Enter a positive integer: ")))
print("\n")
a.greet()
print("\n")
a.square()
a.cube()
a.squareRoot()
