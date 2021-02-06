# Hangman My Version
# Author: Edmon Mancao
# The classic game of hangman. This is all the noun words indicated as a quesiton
# of our game.
#

import random

# constants
HANGMAN = (
    """
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
   ---------
   """,
   """
    ------
    |    |
    |    0
    |
    |
    |
    |
    |
    |
   ---------
   """,
   """
    ------
    |    |
    |    0
    |   -+-
    |
    |
    |
    |
    |
   ---------
   """,
   """
    ------
    |    |
    |    0
    |  /-+-
    |
    |
    |
    |
    |
   ---------
   """,
   """
    ------
    |    |
    |    0
    |  /-+-/
    |
    |
    |
    |
    |
   ---------
   """,
   """
    ------
    |    |
    |    0
    |  /-+-/
    |    |
    |
    |
    |
    |
   ---------
   """,
   """
    ------
    |    |
    |    0
    |  /-+-/
    |    |
    |    |
    |   |
    |   |
    |
   ---------
   """,
   """
    ------
    |    |
    |    0
    |  /-+-/
    |    |
    |    |
    |   | |
    |   | |
    |
   ---------
   """)

MAX_WRONG = len(HANGMAN) - 1