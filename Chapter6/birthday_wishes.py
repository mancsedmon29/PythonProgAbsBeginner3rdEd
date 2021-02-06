# Birthday Wishes
# Demonstreate keywords arguments and default parameter values

# Positional parameters
def birthday1(name, age):
    print('Happy birthday,' , name, "!", " I here you're", age, "today.\n")
    
# Parameters with default values
def birthday2(name = 'Ezequiel', age=1):
    print("Happy birthday,", name, "!", " I hear you're", age, "today.\n")
    
birthday1("Ezequiel", 1)
birthday1(1, "Ezequiel")
birthday1(name = "Jackson", age=1)
birthday1(age = 1, name="Jackson")


birthday2()
birthday2(name="Katherine")
birthday2(age = 12)
birthday2(name = "Katherine", age = 12)
birthday2("Katherine", 12)

input("\n\nPress the enter key to exit.")
