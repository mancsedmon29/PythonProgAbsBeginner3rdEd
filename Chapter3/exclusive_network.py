# Exclusive Network
# Demonstrates logical operators and compound conditions

print("\tExclusive Computer Network")
print("\t\tMembers only!\n")

security = 0

username =""
while not username:
    username = input('Username: ')
    
password =""
while not password:
    password = input('Password: ')
    
if username == "M.Dawson" and password == 'secret':
    print("Hi. Mike.")
    security = 5
elif username == "S.Meier" and password == 'civilization':
    print('Hi. Sid.')
    security = 3
elif username == 'S.Miyamoto' and password == 'mariobros':
    print('What\'s up. Shigeru?')
    security = 3
elif username == "W.Wright" and password == "thesims":
    print("How goes it. Will?")
    security = 3
elif username == "guest" and password == "guest":
    print("Welcome, guest!")
    security = 1
else:
    print("Login failed. You're not so exclusive.\n")

input("\n\nPress enter key to exit.")