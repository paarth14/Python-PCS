# Create a Class Attribute with 'a', create an object from it and set it directly using 'object.a'. Does this change the class attribute.

class Sample:
    a = "Paarth"

obj = Sample()
obj.a = "Vicky" #This will only create an instance attribute.
# Sample.a = "Vicky" # If we will uncomment this line, then it will change the class attribute.

print(Sample.a)
print(obj.a)

# No it will not change the Class Attribute, it will only set the instance attribute.
