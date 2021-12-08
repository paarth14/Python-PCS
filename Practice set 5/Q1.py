# Write a Python program to create a dictionary of Hindi words with their values as english translation. Provide user an option to look it up!

mydict = {
    "tauliya" : "towel",
    "bistar" : "bed",
    "chaaval" : "rice",
    "namak" : "salt"
}

print(list(mydict.items()))

print("Options are: ", mydict.keys())
a = input("Enter the Hindi Word: ")
print("The meaning of the word is: ", mydict[a]) 
