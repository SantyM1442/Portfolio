# This is a guess the number game
import random
secretNumber=random.randint(1,20)
print('I am thinking of a number between 1 and 20')
# Ask the player to guess 6 times
for guessTaken in range(1,7):
    print('Take a guess')
    guess=int(input())
    if guess<secretNumber:
        print('Your guess is too low')
    elif guess > secretNumber:
        print('Your guess is to high')
    else:
        break #this condition is the correct guess
if guess==secretNumber:
    print('Good Job! You guessed my number in '+str(guessTaken)+' guess!')
else:
    print('Nope. The number I was thinking of was '+str(secretNumber))
