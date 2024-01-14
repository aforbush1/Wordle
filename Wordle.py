"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    # Define the maximum number of guesses
    MAX_GUESSES = 6
    current_row = 0
    # Create the WordleGWindow object
    gw = WordleGWindow()

    # Random select from the Array of 5 letter words, set to variable "word_of_the_day".
    word_of_the_day = random.choice(FIVE_LETTER_WORDS).lower()
    word_of_the_day = 'helve'
    print(word_of_the_day)

    # This currently just checks the first word and row
    def enter_action(guess):
        nonlocal current_row

        # Check if the maximum number of guesses has been reached
        if current_row >= MAX_GUESSES:
            gw.show_message("You've reached the maximum number of guesses.")
            return

        for col, letter in enumerate(guess):
            gw.set_square_letter(0, col, letter)

        if(guess.lower() in FIVE_LETTER_WORDS):
            if(guess.lower() == word_of_the_day.lower()):
                for col in range(0, N_COLS):
                    # row needs to be adjusted to be current
                    gw.set_square_color(0, col, CORRECT_COLOR)
                gw.show_message("You guessed the word!")
            else:
                for col in range(0, N_COLS):
                    if(gw.get_square_letter(0, col).lower() == word_of_the_day[col]):
                        gw.set_square_color(0, col, CORRECT_COLOR)
                    elif(gw.get_square_letter(0, col).lower() in word_of_the_day):
                        if(gw.get_square_letter(0, col).lower() in guess[:col]):
                            gw.set_square_color(0, col, MISSING_COLOR)
                        else:
                            gw.set_square_color(0, col, PRESENT_COLOR)
                    else:
                        gw.set_square_color(0, col, MISSING_COLOR)
        elif(guess.lower() not in FIVE_LETTER_WORDS):
            gw.show_message("Not in word list")
            current_row += 1

    a = N_ROWS
    # Set the enter_action function as a callback for the ENTER key
    gw.add_enter_listener(enter_action)
    # a += 1
    # gw.add_enter_listener(enter_action)
    # a += 1
    # gw.add_enter_listener(enter_action)
    # a += 1
    # gw.add_enter_listener(enter_action)
    # a += 1
    # gw.add_enter_listener(enter_action)
    # a += 1

    # #MILESTONE 1
    # # Iterate through the entire matrix
    # for col, letter in enumerate(word_of_the_day):
    #     gw.set_square_letter(0, col, letter)

# Startup code
if __name__ == "__main__":
    wordle()
    # Press the "Enter" key in the terminal to close the program
    input("Press Enter to exit")

