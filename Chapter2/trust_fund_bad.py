# Trust Func Buddy - Bad
# Demonstrates a logical error
print(
"""
            Trust Fund Buddy
    
Totals your monthly spending so that your trust fund doesn't run out
(and you're forced to get a real job).
    
Please enter the request, monthy cost. Since you're rich. ignore pennies and use only dollar amounts.
    
"""
)

car = input('Lamborghini Tunes-Ups: ')
rent = input("Manhattan Apartment: ")
jet = input("Private Jet Rental: ")
gifts = input("Gifts: ")
food = input("Dining Out: ")
staff = input("Staff (buttlers, chef, driver, assistant): ")
guru = input("Personal Guro and Coach: ")
games = input("Computer Games: ")

total = car + rent + jet + gifts + food + staff + guru + games

print("\nGrand Total:", total)

input("\n\nPress the enter key to exit.")



