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
    print(word_of_the_day)
    # This currently just checks the first word
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
                    gw.set_square_color(0, col, CORRECT_COLOR)
                gw.show_message("You guessed the word!")
            else:
                
                # If incorrect, set colors based on correct, present, and missing letters
                for character in word_of_the_day:
                    for char in guess:
                        if(char == character):
                            gw.set_square_color(0, 0, CORRECT_COLOR)
                        elif(char in word_of_the_day):
                            gw.set_square_color(0,0, PRESENT_COLOR)
                        else:
                            gw.set_square_color(0, 0, MISSING_COLOR)
                
                # Set the guessed letters again for visual feedback
                for col, letter in enumerate(guess):
                    gw.set_square_letter(0, col, letter)
                
                current_row += 1

        # If the guess is not in the word list, show a message
        elif(guess.lower() not in FIVE_LETTER_WORDS):
            gw.show_message("Not in word list")
            current_row += 1

    # Set the enter_action function as a callback for the ENTER key
    # gw.set_square_letter(0, 0, 'H')
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

