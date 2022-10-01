import random
import sys
import hangman_stages
from words import words
remaining_attempts = 8

def find_valid_words(words):
    """
This function pulls a random word from the words.py folder, checks
if it has a - or a space in between the word then picks another random word if 
it has one of these. It would could become confusing for the player.
    """
    word = random.choice(words) #pulls a random word from the words.py folder.
    while '-' in word or ' ' in word: #Makes the gam find a work not seperated by ' ' space or '-'
        word = random.choice(words)
    return word



def print_hidden_words(hidden_word, guessed_letters):
    """
    This function pulls the words from the find_valid_words funtion and displays them as a _
    which creates the main function of the hangman game.
    """
    print(" _ " * len(hidden_word)) #changes the words to underscores

def letter_guessing(guess, hidden_word):
    if len(guess) > 1 or not guess.isalpha():
        print("One letter at a time and no numbers please!")
        sys.exit()
    else:
        if guess in hidden_word:
            return True
        else:
            return False
        
if letter_guessing:
    if guess in letter_guessed:
        print("You have already guessed the letter {}".format(guess))
    else:
        print("Yes! The letter {} is part of the secret word".format(guess))
        guessed_letters += guess
else:
    print("No! The letter {} is not part of the secret word".format(guess))
    remaining_attempts -= 1

print(hangman_stages.get_hangman_stages(remaining_attempts))
hidden_word(words)

print("You have already guessed this letter!")

print("Welcome! Hope you enjoy this game of hangman :) \n")
hidden_word = find_valid_words(words)
print(hangman_stages.get_hangman_stages(remaining_attempts))
print_hidden_words(hidden_word)
guess = input("Guess a letter:")
letter_guessed = letter_guessing(guess, hidden_word)