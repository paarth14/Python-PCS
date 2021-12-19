# Create a Class Programmer for storing the information of few programmers working at Microsoft

class Programmer:
    company = "Microsoft"
    
    def __init__(self, name, product):
        self.name = name
        self.product = product
        
    def getInfo(self):
        print(f"The name of the {self.company} Programmer is {self.name} and the product is {self.product}.")
    
emp1 = Programmer("Paarth", "Skype")
emp2 = Programmer("Vansh", "Github")
emp1.getInfo()
emp2.getInfo()
