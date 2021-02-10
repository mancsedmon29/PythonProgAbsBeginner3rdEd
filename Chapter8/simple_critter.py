# Simple Critter
# Demosntrates a basic class and objects

class Critter(object):
    """A Virtual pet"""
    def talk(self):
        print("Hi, I'm an instance of class Critter.")
        
# main
crit = Critter()
crit.talk()

input("\n\nPress the enter key to exit.")