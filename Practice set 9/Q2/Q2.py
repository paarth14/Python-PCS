# The game() in a program lets a user to play a game and returns the score as an integer. You need to read a file 'hiscore.txt' which is either blank or contains the previous Hi-Score.
# We simply need to update the hi-score.

def game():
    return 449

score = game()

with open('hiscore.txt') as f:
    hiscore = int(f.read())

if hiscore<score:
    with open('hiscore.txt', 'w') as f:
        f.write(str(score))
