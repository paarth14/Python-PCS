#Project - 3 : THE PERFECT GUESS.

#Problem Statement :- Write a Program that generates a random number and asks the user to guess it.
#If the player guess is lower than the actual number then it will display "Higher Number Please". 
#If the player guess is Higher than the actual number then it will display "Lower Number Please". 
#At Last when user guess it Correctly then it will display the number of guesses, the player used to arrive that number.
#Also create one hiscore.txt where if number of guesses is less than previous number of guesses then it will write in that
#hiscore.txt file.

import random

randNumber = random.randint(1,100)
userGuess = None
guesses = 0

while(userGuess != randNumber):
    userGuess = int(input("Enter the number: "))
    guesses += 1
    if(userGuess == randNumber):
        print("You, Guessed it Correctly!")
    else:
        if(userGuess > randNumber):
            print("Please, Enter a Smaller number")
        else:
            print("Please, Enter the Larger number")
            
print(f'Congrats! You Guessed the number in {guesses} Guesses.')

with open('hiscore.txt', 'r') as f:
    hiscore = int(f.read())
    
if(guesses<hiscore):
    print("You have just broken the high score!")
    with open('hiscore.txt', 'w') as f:
        f.write(str(guesses))
        
        
