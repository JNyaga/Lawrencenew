import random
from words import words
import string

# # print(random.choice(words))

# alphabet = set(string.ascii_uppercase)
# used = set('joel'.upper())
# print(f'{alphabet} - {used} = ', alphabet-used)

# the program

# first we have to pick a random word from our words


def get_word(words):
    word = random.choice(words)
    while ' ' in word or '_' in word:
        word = random.choice(words)

    return word.upper()

# second we need to guess the ryt letters to our word....
# ...thus the game


def hangman():
    word = get_word(words)
    print(word)
    word_letters = set(word)  # gets letters in word in a set
    alphabet = set(string.ascii_uppercase)  # gets all letters in caps
    used_letters = set()  # what the user has guessed
    lives = 10

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(['a','b','cd']) --> 'a b cd'
        print(f'You have {lives} lives left and used these letters: ', ' '.join(
            used_letters))
        # what is the current word...
        # ...(i.e W - R D)
        # replaces '-'with correct letter
        word_list = [
            letter if letter in used_letters else '-' for letter in word]
        print('Current word:', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet-used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # takes away life if wrong

        elif user_letter in used_letters:
            print('You have arleady used that character. Try again')

        else:
            print('Invalid Character. Try again')

    if lives == 0:
        print('you have lost the word is', word)
    else:
        print('You have guesed the word', word, 'you twat!!')


hangman()
