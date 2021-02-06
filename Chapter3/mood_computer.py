# Mood Computer
# Demonstrates the elif

import random

print('I sense your energy. Your true emotion are coming across my screen.')
print('You are...')

mood = random.randint(1, 3)

if mood == 1:
    # Happy
    print(
            """
            
            -----------
            |         |
            | O     O |
            |   <     |
            |         |
            | .     . |
            |  .   .  |
            |   ...   |
            -----------
            """)
    
elif mood == 2:
    # Neutral
    print(
            """
            
            -----------
            |         |
            | O     O |
            |   <     |
            |         |
            | ------- |
            |         |
            |         |
            -----------
            """)
    
elif mood == 3:
    # Sad
    print(
            """
            
            -----------
            |         |
            | O     O |
            |   <     |
            |         |
            |    .    |
            |   . .   |
            |  .   .  |
            |         |
            -----------
            """)
    
else:
    print("Illegal mood value! (You must be in a really bad mood).")
    
print("...today.")

input("\n\nPress the enter key to exit.")

    
    