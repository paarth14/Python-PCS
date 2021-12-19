# Can you change the self parameter inside a class to something else. Try Changing 'self' to 'slf' and see what happens.

class Change:
    def printData(slf):
        print(f"The name of employee is {slf.name} and age is {slf.age}")
    
employee = Change()
employee.name = "Paarth"
employee.age = 20
employee.printData()

# Yes it, works.
