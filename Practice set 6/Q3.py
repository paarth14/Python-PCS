# A Spam Comment is defined as a text containing following keywords :
# "make a lot of money", "buy now", "subscribe this", "click this". Write a program to detect this Spam Comments ?

cmt = input("Enter your comment: ")

if("make a lot of money" in cmt):
    spam = True
elif("buy now" in cmt):
    spam = True
elif("click this" in cmt):
    spam = True
elif("subscribe this" in cmt):
    spam = True
else:
    spam = False
    
if(spam):
    print("It's an Spam Comment!")
else:
    print("It's not an Spam Comment!")
    
# OUTPUT :-
# Enter your comment: Hello buy now
# It's an Spam Comment!
