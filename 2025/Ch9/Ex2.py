'''
The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
'''

with open("Hi-score.txt", "r") as f:
    hi_score = int(f.read())

score = game()
if score > hi_score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))

print(f"Hi-score is: {hi_score}")
print(f"Your score is: {score}")