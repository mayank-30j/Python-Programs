import random


def play():

    print('What\'s your choice')
    user = input("'P for Paper', 'R for Rock', 'S for Scissor': ")
    computer = random.choice(['r', 'p', 's'])
    print('______________________')
    print('You -------->', user)
    print('Computer --->', computer)
    print('_______________________')
    if user == computer:
        return '\nIt\'s a tie'

    if is_winner(user, computer):
        return '\nYou win'

    return '\nYou lost'


def is_winner(player, opponent):
    # r > s, s > p, p > r
    # if player wins then returns Ture

    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p' or player == 'p' and opponent == 'r':
        return True


chance = int(input('How many turn you want to play for: '))
for i in range(1, chance+1):
    print(play())
