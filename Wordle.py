"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    # Random select from the Array of 5 letter words, set to variable "word_of_the_day".
    word_of_the_day = random.choice(FIVE_LETTER_WORDS).upper()
    print(word_of_the_day)

    def enter_action(guess):
        gw.show_message("Congratulations! You guessed the Word!")

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    # Display the individual letters of the word_of_the_day in the WordleGWindow
    for col, letter in enumerate(word_of_the_day):
        gw.set_square_letter(0, col, letter)

# Startup code
if __name__ == "__main__":
    wordle()
    # Press the "Enter" key in the terminal to close the program
    input("Press Enter to exit")
