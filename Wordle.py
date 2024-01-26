"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

#Import the libraries
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, KEY_COLOR, UNKNOWN_COLOR
import tkinter as tk
from tkinter import messagebox

# Alternate Colors
ALTERNATE_CORRECT_COLOR = "#93CAED"
ALTERNATE_PRESENT_COLOR = "#FAC898"
ALTERNATE_MISSING_COLOR = "#999999"
ALTERNATE_UNKNOWN_COLOR = "#FFFFFF"
ALTERNATE_KEY_COLOR = "#DDDDDD"

#Define opening function
def wordle():
    gw = WordleGWindow()

    # Ask the user if they want to use alternate colors using a messagebox
    use_alternate_colors = messagebox.askyesno("Color Choice", "Would you like to use alternate colors?", default='no')
    gw._root.focus_force()

    # Check if the user wants to use alternate colors
    if use_alternate_colors:
        #Change the colors to a blue-orange color scheme
        global CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, KEY_COLOR, UNKNOWN_COLOR
        CORRECT_COLOR = ALTERNATE_CORRECT_COLOR
        PRESENT_COLOR = ALTERNATE_PRESENT_COLOR
        MISSING_COLOR = ALTERNATE_MISSING_COLOR
        KEY_COLOR = ALTERNATE_KEY_COLOR
        UNKNOWN_COLOR = ALTERNATE_UNKNOWN_COLOR

    # Random select from the Array of 5 letter words, set to variable "word_of_the_day".
    word_of_the_day = random.choice(FIVE_LETTER_WORDS)

    # Function to end the program
    def exit_program(event=None):
        # Destroys the window and ends the program
        gw._root.destroy()

    # Function for [ENTER]
    def enter_action(guess):
        # Get the current row
        current_row = gw.get_current_row()
        guess_length = 0
        # Create local variables
        word = []
        green = []

        #Set the letters in the squares
        for col, letter in enumerate(guess):
            gw.set_square_letter(current_row, col, letter)
            
            # Make sure it's a five-letter word
            if(letter != " "):
                guess_length += 1

        #Create a list to keep track of the word
        for char in word_of_the_day:
            word.append(char)
        
        # Check if the guess is a five-letter word
        if (guess_length == 5):
            # Lowercase guess variable
            guess = guess.lower()

            #Check if guess is in the dictionary (aka is a word)
            if(guess in FIVE_LETTER_WORDS):
                # if yes, then see if it is the word of the day
                if(guess == word_of_the_day):
                    #If yes, then color it appropriately
                    for col in range(0, N_COLS):
                        #Color the squares correctly
                        gw.set_square_color(current_row, col, CORRECT_COLOR)

                        #Make sure to color the keys right
                        for letter in guess:
                            gw.set_key_color(letter.upper(), CORRECT_COLOR)

                    # If the user guesses it, then congratulate them
                    gw.show_message(f"You got it in {current_row + 1} {'try' if current_row == 0 else 'tries'}! Press any key to exit.")
                    #End the program
                    gw._root.bind("<KeyPress>", exit_program)
                else:
                    # Get results for each character in the guess
                    for col, char in enumerate(guess):
                        #Update for green by comparing guess string to word of day strings
                        if(char == word[col]):
                            # Send matches to a list
                            green.append(col)
                            guess_word = []

                            # Green is applied over anything
                            if(gw.get_key_color(char.upper()) in {KEY_COLOR,UNKNOWN_COLOR,PRESENT_COLOR}):
                                gw.set_key_color(char.upper(),CORRECT_COLOR)

                            for character in guess:
                                guess_word.append(character.lower())
                            
                            guess_word[col] = char.upper()
                            guess = "".join(guess_word)

                            #Replace value on the word list so that it won't be counted again
                            word[col] = "*"

                    for col, char in enumerate(guess):
                        # If the character is in the daily word, then do stuff
                        if(char in word):
                            # Make everything yellow for now
                            gw.set_square_color(current_row, col, PRESENT_COLOR)

                            # Make sure the keys don't change color to gray; they can change to green (see ahead)
                            if(gw.get_key_color(char.upper()) in {KEY_COLOR,UNKNOWN_COLOR,PRESENT_COLOR}):
                                gw.set_key_color(char.upper(),PRESENT_COLOR)

                            #Replace value on the word list so that it won't be counted again
                            if(word.count(char) < guess.count(char)):
                                word[word.index(char)] = "*"
                        # Otherwise, color gray
                        else:
                            gw.set_square_color(current_row, col, MISSING_COLOR)

                            #Once gray, forever gray
                            if(gw.get_key_color(char.upper()) in {KEY_COLOR,UNKNOWN_COLOR}):
                                gw.set_key_color(char.upper(),MISSING_COLOR)

                    # Output and display the green; it will overlay on the yellow
                    for item in green:
                        gw.set_square_color(current_row, item, CORRECT_COLOR)

                # iterate the rows by one
                current_row += 1
            
                # Check if the game has reached its last guess
                if current_row == N_ROWS:
                    if guess.lower() != word_of_the_day.lower():
                        # If the user doesn't guess it, then show the answer
                        gw.show_message(f"Wordle is {word_of_the_day.upper()}. Press any key to exit.")
                        #End the program
                        gw._root.bind("<KeyPress>", exit_program)
            #Otherwise, show error message
            else:
                gw.show_message("Not in word list")
        else:
            gw.show_message("Enter a 5-letter word")

        # Make sure that we don't overextend the row boundary
        if(current_row < N_ROWS):
            # Keep the row accurate
            gw.set_current_row(current_row)

    # Set the enter_action function as a callback for the ENTER key
    gw.add_enter_listener(enter_action)

#****************************************************************
    # #MILESTONE 1
    # # Iterate through the entire matrix
    # for col, letter in enumerate(word_of_the_day):
    #     gw.set_square_letter(0, col, letter)
#****************************************************************

# Startup code
if __name__ == "__main__":
    #Get the program started
    msg = tk.Tk()
    msg.withdraw()  # Hide the main window

    wordle()

    # Press the "Enter" key in the terminal to close the program
    input("Press Enter to exit")