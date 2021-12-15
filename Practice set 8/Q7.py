# Write a Python function to remove a given word from a list and strip it at the same time.

def remove_and_split(string, word):
    newStr = string.replace(word, " ")
    return newStr.strip()
    
this = "      Paarth is a good boy       "
print(remove_and_split(this, "Paarth"))
