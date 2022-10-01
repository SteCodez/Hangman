import random
import sys
import hangman_stages
from words import words
remaining_attempts = 8
guessed_letters = ""

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



def print_hangman_word(words, guessed_letters):
    """
    This function pulls the words from the find_valid_words funtion and displays them as a _
    which creates the main function of the hangman game.
    """
    for letter in words:
        if letter in guessed_letters:
            print(" {} ".format(letter), end="")
        else:
            print(" _ ", end="")
    print("\n")
    
def get_unique_letters(word):
    return "".join(set(word))   
    
def letter_guessing(guess, words):
    if len(guess) > 1 or not guess.isalpha():
        print("One letter at a time and no numbers please!")
        sys.exit()
    else:
        if guess in words:
            return True
        else:
            return False
        
while remaining_attempts > 0 and len(guessed_letters) < len(get_unique_letters(words)):
    guess = input("Guess a letter: ")
    guessed_letters = letter_guessing(guess, words)   
    if guess in guessed_letters:
        print("You have already guessed the letter {}".format(guess))
    else:
        print("Yes! The letter {} is part of the secret word".format(guess))
        guessed_letters += guess
else:
    print("No! The letter {} is not part of the secret word".format(guess))
    remaining_attempts -= 1

print(hangman_stages.get_hangman_stages(remaining_attempts))
print("Welcome! Hope you enjoy this game of hangman :) \n")
print(hangman_stages.get_hangman_stages(remaining_attempts))
print_hangman_word(words, guessed_letters)
words = find_valid_words(words)