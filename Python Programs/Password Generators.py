import random

print('Welcome to your Password Generator\n ')

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@!#$%^&.,*()_'

number = int(input('Number of passwords to  generate: '))

length = int(input('Length of your password: '))

print('\n Here are the passwords computer generated ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(char)
    print('--------->   ', passwords)
