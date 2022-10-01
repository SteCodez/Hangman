import random
from words import words

def find_valid_words(words):
    """
This function pulls a random word from the words.py folder, checks
if it has a - or a space in between the word then picks another random word if 
it has one of these. It would could become confusing for the player.
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word