"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

#Import the libraries
import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, KEY_COLOR, UNKNOWN_COLOR

#Define opening function
def wordle():
    # Define the maximum number of guesses
    MAX_GUESSES = 6
    # Create the WordleGWindow object
    gw = WordleGWindow()
    # Set the get_current_row() function to variable
    current_row = gw.get_current_row()
    # Random select from the Array of 5 letter words, set to variable "word_of_the_day".
    word_of_the_day = random.choice(FIVE_LETTER_WORDS).lower()

    # Function for [ENTER]
    def enter_action(guess):
        # Call global variable
        nonlocal current_row

        if current_row >= MAX_GUESSES:
            gw.show_message(f"The word of the day is {word_of_the_day.upper()}")
            return
        
        # Create local variables
        word = []
        green = []

        #Set the letters in the squares
        for col, letter in enumerate(guess):
            gw.set_square_letter(current_row, col, letter)

        #Create a list to keep track of the word
        for char in word_of_the_day:
            word.append(char)
            
        #Check if guess is in the dictionary (aka is a word)
        if(guess.lower() in FIVE_LETTER_WORDS):
            # if yes, then see if it is the word of the day
            if(guess.lower() == word_of_the_day.lower()):
                #If yes, then color it appropriately
                for col in range(0, N_COLS):
                    #Color the squares correctly
                    gw.set_square_color(current_row, col, CORRECT_COLOR)

                    #Make sure to color the keys right
                    for letter in guess:
                        gw.set_key_color(letter, CORRECT_COLOR)

                #Huzzah magic powers
                gw.show_message(f"You guessed the word! It took you {current_row + 1} tries")
                return

            else:
                # Get results for each character in the guess
                for col, char in enumerate(guess.lower()):
                    #Update for green by comparing guess string to word of day strings
                    if(char == word[col]):
                        # Send matches to a list
                        green.append([col,char])

                        # Green is applied over anything
                        if(gw.get_key_color(char.upper()) in {KEY_COLOR,UNKNOWN_COLOR,PRESENT_COLOR}):
                            gw.set_key_color(char.upper(),CORRECT_COLOR)
                    # If the character is in the daily word, then do stuff
                    if(char in word):
                        # Make everything yellow for now
                        gw.set_square_color(current_row, col, PRESENT_COLOR)

                        # Make sure the keys don't change color to gray; they can change to green (see ahead)
                        if(gw.get_key_color(char.upper()) in {KEY_COLOR,UNKNOWN_COLOR,PRESENT_COLOR}):
                            gw.set_key_color(char.upper(),PRESENT_COLOR)

                        #Replace value on the word list so that it won't be counted again
                        if(word.count(char) < guess.count(char.upper())):
                            word[word.index(char)] = "*"
                    # Otherwise, color gray
                    else:
                        gw.set_square_color(current_row, col, MISSING_COLOR)

                        #Once gray, forever gray
                        if(gw.get_key_color(char.upper()) in {KEY_COLOR,UNKNOWN_COLOR}):
                            gw.set_key_color(char.upper(),MISSING_COLOR)

                # Output and display the green; it will overlay on the yellow
                for item in green:
                    gw.set_square_color(current_row, item[0], CORRECT_COLOR)      

            # iterate the rows by one
            current_row += 1
        
        # Check if the game has reached its last guess
        if current_row == MAX_GUESSES:
            if guess.lower() != word_of_the_day.lower():
                gw.show_message(f"The Word of the day is {word_of_the_day}")

            # This will end the game by not allowing more guesses
            return

        elif guess.lower() not in FIVE_LETTER_WORDS:
            gw.show_message("Not in word list")
        
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
    wordle()
    # Press the "Enter" key in the terminal to close the program
    input("Press Enter to exit")