"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    # Create the WordleGWindow object
    gw = WordleGWindow()
    # Random select from the Array of 5 letter words, set to variable "word_of_the_day".
    word_of_the_day = random.choice(FIVE_LETTER_WORDS).upper()

    # This currently just checks the first word
    def enter_action(guess):
        if(guess.lower() in FIVE_LETTER_WORDS):
            gw.show_message("You guessed the word!")
        elif(guess.lower() not in FIVE_LETTER_WORDS):
            gw.show_message("Not in word list")

    # Call the function
    gw.add_enter_listener(enter_action)

    # #MILESTONE 1
    # # Iterate through the entire matrix
    # for col, letter in enumerate(word_of_the_day):
    #     gw.set_square_letter(0, col, letter)

# Startup code
if __name__ == "__main__":
    wordle()
    # Press the "Enter" key in the terminal to close the program
    input("Press Enter to exit")
