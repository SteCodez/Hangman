import random
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



def print_hidden_words(hidden_word):
    """
    This function pulls the words from the find_valid_words funtion and displays them as a _
    which creates the main function of the hangman game.
    """
    print(" _ " * len(hidden_word)) #changes the words to underscores

print("Welcome! Hope you enjoy this game of hangman :) \n")
hidden_word = find_valid_words(words)
print(hangman_stages.get_hangman_stages(remaining_attempts))
print_hidden_words(hidden_word)