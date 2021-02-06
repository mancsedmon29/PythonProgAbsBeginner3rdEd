# Hero's Inventory 3.0
# Demonstrates lists

# Create a list with some itmes and display with a for loop
inventory = ["sword", "armor", "shield", "healing potion"]
print('Your items:')
for item in inventory:
    print(item)
    
input('\n\nPress enter key to continue.')

# get the length of a list
print("You have", len(inventory), "items in you possession.")

input("\nPress the enter key to continue.")

# test for membership with in
if 'healing potion' in inventory:
    print('You will live to fight another day.')
    
# display one item through an index
index = int(input('\nEnter the index number for an item in inventory: '))
print("At index", index, "is", inventory[index])

# display a slice
start = int(input("\nEnter the index number to begin a slice: "))
finish = int(input("Enter the index number to end the slice: "))
print("inventory[", start, ":", finish, "] is", end='')
print(inventory[start:finish])

input('\nPress the enter key to continue.')

# concatenate two list
chest = ['gold', 'gems']
print("You find a chest which contains:")
print(chest)
print("You add the contents of teh chest to your inventory.")
inventory += chest
print("You inventory is now")
print(inventory)

input("\nPress the enter key to continue.")

# Assigned by index
print("You trade your sword for a crossbow.")
inventory[0] = 'crossbow'
print('Your inventory is now:')
print(inventory)

input('\nPress the enter key to continue.')

# Assigned by slice:
print("You use your gold and gems to buy an orb of future telling.")
inventory[4:6] = ["orb of future telling"]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

# delete an element
print("In a great battle, your shield is destroyed.")
del inventory[2]
print('Your inventory is now:')
print(inventory)

input("\nPress the enter key to continue.")

# delete a slice
print('Your cross bow and armore are stolen by thieves.')
del inventory[:2]
print("Your inventory is now:")
print(inventory)

input("\nPress the enter key to continue.")

