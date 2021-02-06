# Instruction
# Demonstrates programmer-created
'''
display the game instructions
determine who goes first
create an empty tic-tac-toe board
display the board
while nobody’s won and it’s not a tie
    if it’s the human’s turn
        get the human’s move
        update the board with the move
    otherwise
        calculate the computer’s move
        update the board with the move
    display the board
    switch turns
congratulate the winner or declare a tie
'''
def instructions():
    """display game instructions."""
    print(
    """
    Welcome to the greatest intellectual challange of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.
    
    You will make your move know by entering a number, 0 - 8. The number
    will correspond to the board position as illustrated:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
                    
    Prepare youruself, human. The ultimate battle is about to begin. \n
    """
    )
    
# main
print('Here are the instructions to the Tic-Tac-Toe game:')
instructions()
print('Here they are again:')
instructions()
print("You probably understand the game by now.")

input("\n\nPress the enter key to exit.")
