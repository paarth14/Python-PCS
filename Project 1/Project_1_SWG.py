# Game 1 :- Snake, Water, Gun - Game.
# Write a Python Program to create a Snake, Water & Gun Game and it will be Computer vs Human.

#Game 1 :- Snake, Water, Gun

import random

def gameWin(comp, player):
    #If two values are equal declare a tie!
    if(comp == player):
        return None
    
    #Check for all possibilities when computers choose 's'
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    
    #Check for all possibilities when computers choose 'w'
    elif comp == 'w':
        if player == 'g':
            return False
        elif player == 's':
            return True
            
    #Check for all possibilities when computers choose 'g'
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True

print("Computer's Turn : Snake (s), Water (w) & Gun (g)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'
    
player = input("Your Turn: Snake (s), Water (w), Gun (g)?: ")
a = gameWin(comp, player)

# Displaying the choices taken by Computer and Player.
print(f"Computer selected: {comp}")
print(f"You selected: {player}")

# Game winning Conditions.
if a == None:
    print("The Game is Tie!")
elif a:
    print("Congo, You Won!")
else:
    print("Sorry, You Lose!")


