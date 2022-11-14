import random as ramd
import string
import os

from words import words
from hanged_visual import lives_visual_dict

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def valid_word(words):
    word = ramd.choice(words)
    while '-' in word or ' ' in word:
        word = ramd.choice(words)

    return word.upper()

def hangman():
    word = valid_word(words)
    word_leters = set(word)
    alpha = set(string.ascii_uppercase)
    used_letters = set()

    chances = 6

    while len(word_leters) > 0 and chances > 0:
        clear_screen()
        print(lives_visual_dict[chances])
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))
        print("You still have", chances, "chances and the letters you used so far are: ", ' '.join(used_letters))

        user_letter = input('Please, guess a letter: ').upper()
        if user_letter in alpha - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_leters:
                word_leters.remove(user_letter)
            else:
                chances -= 1
                print(f'The letter {user_letter} is not in the word.')
        elif user_letter in used_letters:
            print('You already used that letter! Guess another letter.')
        else:
            print("That's not a valid letter. Try again.")


    if chances == 0:
        print(lives_visual_dict[chances])
        print(f'You died! The correct word was {word}')
    else:
        print(f"You guessed the {word} correctly!")


if __name__ == '__main__':
    hangman()