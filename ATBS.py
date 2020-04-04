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
#### Chapter 2 pg 52 Rock, Paper, Scissors

import random

print('Rock, Paper, Scissors')
wins = 0
losses = 0 
ties = 0

while True:
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    key = input()

    ai_roll = random.randint(1, 3)
    ai_move = ''

    if ai_roll == 1:
        ai_move = 'r'
    elif ai_roll == 2:
        ai_move = 'p'
    else:
        ai_move = 's'

    # Display player move
    if key == 'r':
        print('Rock vs ...')
    if key == 'p':
        print('Paper vs ...')
    if key == 's':
        print('Scissors vs ...')

    # Display AI move
    if ai_move == 'r':
        print('Rock')
    if ai_move == 'p':
        print('Paper')
    if ai_move == 's':
        print('Scissors')

    # Calculate and display outcome
    if key == ai_move:
        print('It is a tie!')
        ties += 1
    if key == 'r' and ai_move == 'p':
        print('You Lose!')
        losses += 1
    if key == 'r' and ai_move == 's':
        print('You Win!')
        wins += 1
    if key == 'p' and ai_move == 's':
        print('You Lose!')
        losses += 1
    if key == 'p' and ai_move == 'r':
        print('You Win!')
        wins += 1
    if key == 's' and ai_move == 'r':
        print('You Lose!')
        losses += 1
    if key == 's' and ai_move == 'p':
        print('You Win!')
        wins += 1
    if key == 'q':
        break
        
###############
#### Chapter 3 page 74 Zig Zag

import time, sys

def print_row(indent):
    line = ''

    for _ in range(indent):
        line += ' '
    line += '********'
    return line


# Starting Position and direction
indent = 4
backwards = True


while True:

    print(print_row(indent))
    time.sleep(0.03)  # Pause for 0.01 second


    if backwards and indent != 0:
        indent -= 1
    elif indent == 0:
        indent += 1
        backwards = False
    elif not backwards and indent != 4:
        indent += 1
    elif indent == 4:
        indent -= 1
        backwards = True
    else:
        break
        
        
#######################################
#### Chapter 3 page 76 Collatz Sequence
#### With input validation

while True:
    try:
        number = int(input('Enter a number '))
    except ValueError:
        print('You didn\'t enter a number')
        continue
    break

print('The number you entered is:', number)

while number != 1:
    if number % 2 == 0:
        number = int(number / 2)
    else:
        number = number * 3 + 1
    print(str(number))

    
#########################################
#### Chapter 4 Coin Flip Streaks

import random

number_of_streaks = 0
current_streak = 1
experiment = []
flips


for i in range(flips):
    flip = random.randint(1, 2)
    if flip == 1:
        experiment.append('H')
    else:
        experiment.append('T')
    #print('Roll (' + str(i) + ') ----- ' + experiment[i])

    if i > 0:
        if experiment[i] == experiment[i - 1]:
            current_streak += 1
            # print('*****On a streak! #: ' + str(current_streak))
        else:
            #print('*****Streak ended (' + str(current_streak) + ')')
            current_streak = 0

    if current_streak >= 6:
        #print('Streak reached 6! (' + experiment[i] + ')')
        number_of_streaks += 1


# print(experiment)
print(str(number_of_streaks))


# for experiment_number in range(1000):
# Code that creates a list of 100 heads or tails values
# flip = random.randint(1, 2)
# code that checks if there is a streak of 6 heads or tails in a row.
#######################################

