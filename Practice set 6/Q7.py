# Write a python program to find out whether the given post is about "Harry" or not ?

post = input("Enter a name: ")
name = "Harry"

if(name.lower() or name.upper() in post):
    print("This post is about Harry")
else:
    print("This post is not about Harry")
    
