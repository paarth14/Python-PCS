# Write a python program to greet all the person names stored in a list l1 which starts with letter "S".
# l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

l1 = ["Harry", "Sohan", "Sachin", "Rahul"]

for name in l1:
    if name.startswith("S"):
        print("Hello", name)
