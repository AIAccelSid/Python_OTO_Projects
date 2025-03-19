# -*- coding: utf-8 -*-
"""The Hangman Rescue Mission.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JN9f_-SeQBvZWmLKoZ1g71beEwndg8Bc

Objective: Create a text-based Hangman game.

You’ve just been transported into a magical kingdom where words hold the power to save or doom someone. An evil wizard has captured a poor soul; the only way to free them is by guessing the secret word. Each wrong guess brings the prisoner closer to their fate. Use your code to build this classic game and save the day!

Task:

Choose a word randomly from a list.
Display underscores for each letter and update with correct guesses.
Limit incorrect guesses to a set number.

Solution:

Use a word list, loops, and string manipulation to manage guesses and the display.
Key Concepts: Loops, conditionals, random module, lists, string manipulation.

***Solution :-***
"""

import random

# List of words to choose from
word_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Number of incorrect guesses allowed
guess_limit = 6

def hangman():
    # Choose a random word from the list
    secret_word = random.choice(word_list)

    # Initialize the display with underscores for each letter
    display = ["_"] * len(secret_word)

    # Initialize the number of incorrect guesses
    incorrect_guesses = 0

    print("Welcome to Hangman You have {} chances to guess the word.".format(guess_limit))

    while True:
        # Display the current state of the word
        print(" ".join(display))

        # Ask for a guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is a single letter
        if len(guess) != 1:
            print("Please guess one letter at a time.")
            continue

        # Check if the guess is in the secret word
        if guess in secret_word:
            # Update the display with the correct guess
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    display[i] = guess
        else:
            # Increment the number of incorrect guesses
            incorrect_guesses += 1
            print("Incorrect guess. You have {} chances left.".format(guess_limit - incorrect_guesses))

            # Check if the game is over
            if incorrect_guesses == guess_limit:
                print("Game Over The secret word was {}.".format(secret_word))
                break

        # Check if the word has been fully guessed
        if "_" not in display:
            print(" ".join(display))
            print("Congratulations You've saved the prisoner!")
            break

# Start the game
hangman()

