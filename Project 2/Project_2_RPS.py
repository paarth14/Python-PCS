# Write a Python Program to create a Rock, Paper & Scissor game and it will be Computer vs Human.

# Game 2 - Rock, Paper & Scissor

import random

def game_win(comp, player):
    #If both of them Selected the same choice
    if (comp == player):
        return None
        
    #Possibilities when Computer Selected 'r'
    elif (comp == 'r'):
        if (player == 's'):
            return False
        elif (player == 'p'):
            return True
            
    #Possibilities when Computer Selected 'p'
    elif (comp == 'p'):
        if (player == 'r'):
            return False
        elif (player == 's'):
            return True
            
    #Possibilities when Computer Selected 's'
    elif (comp == 's'):
        if (player == 'r'):
            return True
        elif (player == 'p'):
            return False
    
    

print("Computer's Turn: Rock (r), Paper (p), Scissor (s)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

#Now taking input from player
player = input("Your Turn: Rock (r), Paper (p), Scissor (s)?: ")
a = game_win(comp, player)

print(f"Computer Selected: {comp}")
print(f"You Selected: {player}")

if a == None:
    print("The Game is Tied !!")
elif a:
    print("Congo, You Won!")
else:
    print("You Lose!")
