# Heroe's Inventory
# Demonstration tuple creation

# Create an empty tuple
inventory = ()

# treat the tuple as a condition
if not inventory:
    print("You are empty-handed.")
    
input('\nPress the enter key to continue.')

# create a tuple with some items
inventory = ("sword",
             "armor",
             "shield",
             "healing potion")

# print the tuple
print("\nThe tuple inventory is:")
print(inventory)

# print each element of the tuple
print("\nYour items:")
for item in inventory:
    print(item)
    
input('\n\nPress the enter key to exit.')


