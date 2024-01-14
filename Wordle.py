"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, KEY_COLOR

def wordle():
    # Define the maximum number of guesses
    MAX_GUESSES = 5
    # Create the WordleGWindow object
    gw = WordleGWindow()
    # Set the get_current_row() function to variable
    current_row = gw.get_current_row()
    # Random select from the Array of 5 letter words, set to variable "word_of_the_day".
    word_of_the_day = random.choice(FIVE_LETTER_WORDS).lower()

    #temp stuff delete later
    word_of_the_day = 'sheet'
    print(word_of_the_day)

    # Function for [ENTER]
    def enter_action(guess):
        # Call global variable
        nonlocal current_row
        # Create local variables
        word = []

        for col, letter in enumerate(guess):
            gw.set_square_letter(current_row, col, letter)

        for char in word_of_the_day:
            word.append(char)

        if(current_row <= MAX_GUESSES):
            if(guess.lower() in FIVE_LETTER_WORDS):
                if(guess.lower() == word_of_the_day.lower()):
                    for col in range(0, N_COLS):
                        gw.set_square_color(current_row, col, CORRECT_COLOR)

                        for letter in guess:
                            gw.set_key_color(letter, CORRECT_COLOR)

                    gw.show_message("You guessed the word!")
                else:
                    for col, char in enumerate(guess.lower()):
                        if (char in word):
                            if(col == word.index(char)):
                                gw.set_square_color(current_row, col, CORRECT_COLOR)

                                if(gw.get_key_color == KEY_COLOR):
                                    gw.set_key_color(char.upper(),CORRECT_COLOR)
                            else:
                                gw.set_square_color(current_row, col, PRESENT_COLOR)

                                if(gw.get_key_color == KEY_COLOR):
                                    gw.set_key_color(char.upper(),CORRECT_COLOR)
                            
                            word[word.index(char)] = "*"
                        else:
                            gw.set_square_color(current_row, col, MISSING_COLOR)

                            if(gw.get_key_color == KEY_COLOR):
                                gw.set_key_color(char.upper(),CORRECT_COLOR)

                current_row += 1
            elif(guess.lower() not in FIVE_LETTER_WORDS):
                gw.show_message("Not in word list")
    
            gw.set_current_row(current_row)
        #elif(current_row == MAX_GUESSES):
            #gw.show_message("You've reached the maximum number of guesses.")
            #return

    # Set the enter_action function as a callback for the ENTER key
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