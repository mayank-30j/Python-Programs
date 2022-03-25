# This is a number Guessing game
import time
import time as t
import random

def guess_game():
    points = 0  # Points rewarded to user
    chance = 3  # Number of time user can guess the number

    print('Welcome to Number Guessing game :) ')
    t.sleep(3)

    print('\nYou have to guess a number between 1 and 100 ',
          'if the number is correct you will be rewarded with points ')
    t.sleep(5)

    print('You will also get some hints \n')
    t.sleep(3)

    print("Let's start the game")
    num = random.randint(1, 100+1)

    if num % 2 == 0:
        print("\nHint ----> ", 'number is an even number')

    else:
        print("\nHint ----> ", 'number is an odd number')

    while chance > 0:
        print('\nyou only have {} chances'.format(chance))

        guess = input('Guess the number: ')

        if chance == 3:

            if guess == num:
                print("\nYou guessed it right :)")
                print('You are soooo lucky, you guessed it on your first try ')
                print(" hurreyyyyyyy ")
                print(emoji.emojize(":grinning_face_with_big_eyes:"))
                points += 1
                time.sleep(2)
                print('\nPoints awarded: {}\n'.format(points))
                break
            else:
                print('\nNope this is not the number :( ')
                print('Try again, I am sure you can do it')
                print(emoji.emojize('sad_face'))
                points -= 1
                print('Points awarded: {}\n'.format(points))

        elif chance == 2:

            if guess == num:
                print('\nBraaaaaavoooooo')
                print("What did I said, you can do it :)")
                print(" hurreyyyyyyy")
                points += 1
                print('Points awarded: {}\n'.format(points))
                break

            else:
                print('\nNope this is not the number :( ')
                time.sleep(1)
                print('you only have 1 more chance')
                points -= 1
                print('Points awarded: {}\n'.format(points))

        elif chance == 1:

            if guess == num:
                print('\nFwwweeeeee')
                print("You guessed it right")
                points += 1
                print('Points awarded: {}\n'.format(points))
                break

            else:
                print('\nNope this is not the number :( ')
                points -= 1
                print('Points awarded: {}\n'.format(points))

        chance -= 1
    print('Number was {}'.format(num))
