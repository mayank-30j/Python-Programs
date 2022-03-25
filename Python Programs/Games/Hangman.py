import random
import string
from Words import words  # Words is a file containing list named words, which I copied from one of the GitHub account


def guess_valid_words(wrd):  # randomly chooses words from the list
    word = random.choice(wrd)
    while '-' in word or ' ' in word:
        word = random.choice(wrd)

    return word.upper()


def hangman():
    word = guess_valid_words(words)
    temp_word = word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()  # Letter guessed by users

    # User input
    while len(word_letters) > 0:
        # letters used
        if len(used_letter) > 0:
            print('You have used these letters: ', ' '.join(used_letter))

        # what current words is
        word_list = [letter if letter in used_letter else '-' for letter in word]
        print('Current Words: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letter:
            print('You have already used that character. Pls try again')

        else:
            print('Invalid character. pls tey again')

    print('The word is: ', temp_word)
# gets here when words_letter == 0

hangman()
