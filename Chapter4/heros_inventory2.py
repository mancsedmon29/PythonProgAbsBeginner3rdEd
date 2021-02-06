# Hero's Inventoryf 2.0
# Demonstrate tuples

# create a tuple with some items and display with a for loop
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print each element of the tuple
print("\nYour items:")
for item in inventory:
    print(item)
    
input('\n\nPress the enter key to continue.')

# get the length of the tuple
print("You have", len(inventory), 'items in your possession.')

input("\n\nPress the enter key to continue")

if "healing potion" in inventory:
    print('You will live to fight another day.')

print("""
            Slicing Cheatsheet for "inventory" (Indexing)
            
                 0        1          2             3          
            +--------+---------+----------+------------------+
            |'sword' | 'armor' | 'shield' | 'healing potion' |
            +--------+---------+----------+------------------+
                -4       -3         -2            -1
      """)

# display on item through an index
index = int(input('\nEnter the index number for an item in inventory: '))
print("At index", index, "is", inventory[index])
print("""
            Slicing Cheatsheet for "inventory" (Slicing)
            
            0        1         2          3                  4 
            +--------+---------+----------+------------------+
            |'sword' | 'armor' | 'shield' | 'healing potion' |
            +--------+---------+----------+------------------+
           -4       -3        -2         -1
      """)

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to the end the slice: "))
print("inventory[", start, ":", finish, "] is", end=' ')
print(inventory[start:finish])

input("\n\nPress enter key to exit.")