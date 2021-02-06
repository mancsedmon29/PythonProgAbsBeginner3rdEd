# My version of my Jumbled letter
# Title: Jumbled Letter
# Creator: Edmon Mancao
from random import *

adjective = ('magic', 'beautiful', 'colorful', 'ugly', 'cold', 'small')
adjwords = choice(adjective)
correct = adjwords
jumble = ""

while adjwords:
    position = randrange(len(adjwords))
    jumble += adjwords[position]
    adjwords + adjwords[:position] + adjwords[position+1:]
    
# Start the game
    
print(
    """
                  Welcome to Word Jumble!
        
           Unscramble the letters to make word.
        (Press the enter key at the prompt to quit.)
    """
    )
print('The jumble is:', jumble)

guess = input("\nWhat is your guess?")

while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
    
    if guess == correct:
        print("That's it! You guessed it!\n")
        
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
    



