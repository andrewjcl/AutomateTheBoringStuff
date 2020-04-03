# https://automatetheboringstuff.com/


###### Chapter 2 page 49 - Guess the Number
import random

print('I am thinking of a number between 1 and 20.')
print('Take a guess.')

number = random.randint(1, 20)
attempts = 0

guess = int(input())
attempts += 1

while guess != number:
    if guess > number:
        print('Your guess is too high.')
    else:
        print('Your guess it too low.')
    attempts += 1
    guess = int(input())

print('Good job! You guessed my number in ' + str(attempts) + ' guesses.')

#################################

