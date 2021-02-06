# Word Jumble
#
# The computer pics a random word and then "jumbles" it
# The payer has to guess the original word

from random import *

WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
word = choice(WORDS)

# create a variable to use later to see if the guess is correct
correct = word
jumble = ""

while word:
    position = randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]
    
# start the game
print(
    """
                   Welcome to Word Jumble!
        
            Unscramble the letters to make word.
        (Press the enter key at the prompt to quit.)
    """
    )
print('The jumble is:', jumble)

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    guess = input("Your guess: ")
    
    if guess == correct:
        print("That's it! You guessed it!\n")
        
print("Thanks for playing.")

input("\n\nPress the enter key to exit.")
    