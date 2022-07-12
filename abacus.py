import os

# python 3.8.10
# A CLI Abacus app

# Functions
def display_title_bar(abacus_base):
    # Display the title bar together with the base of the Abacus
    os.system('clear')
    print("--------------------------------")
    print("- Abacus - Base: %d" % abacus_base)
    print("--------------------------------")

def get_abacus_base():
    abacus_base = input("Enter base of abacus [1-n, Q]:\n> ")
    return abacus_base

def get_max_number(abacus_base):
    # Returns the maximum number the user can enter relative to the base of the Abacus
    max_number = (10**abacus_base)
    max_number -= 1
    return max_number

def get_abacus_number(abacus_base):
    # Get user input and check if it's valid and can be represented within the base of the Abacus
    max_number = get_max_number(abacus_base)
    abacus_number = max_number + 1
    invalid_input = False
    while abacus_number > max_number:
        if invalid_input:
            print("Invalid input. Please try again.")
            invalid_input = False
        try:    
            print("Enter number [1-%s, Q]:" % max_number)
            abacus_number = input("> ")
            if abacus_number == "Q":
                return "Q"
            abacus_number = int(abacus_number)
        except Exception:
            abacus_number = max_number + 1
        if abacus_number > max_number:
            invalid_input = True
    abacus_number = str(abacus_number)
    return abacus_number

def display_abacus(abacus_numbers):
    # Display user input to the Abacus bar
    print("- ", end="")
    print("".join(abacus_numbers), end=" in Abacus:\n")
    print("--------------------------------")
    for index, abacus_number in enumerate(abacus_numbers):
        abacus_numbers[index] = int(abacus_number)
        unused_beads = 9 - abacus_numbers[index]
        print("* |", end="")
        print("x"*abacus_numbers[index], end="")
        print("---", end="")
        print("x"*unused_beads, end="|\n")
    print("--------------------------------")

def abort_message():
    print("Quitting... Bye, bye.")

# Main program
# Intialize variables
choice = " "
abacus_base = 0
invalid_input = False
got_input = True

while choice != "Q":
    display_title_bar(abacus_base)
    
    # Display a message if the user input is invalid
    if invalid_input:
        print("Invalid Input. Please try again.")
        invalid_input = False

    # Get user input for the Abacus base. Program closes if the user entered "Q" (quit)
    choice = get_abacus_base()
    if choice == "Q":
        got_input = False
        abort_message()
        break
    try:
        abacus_base = int(choice)
        choice = "Q"
    except Exception:
        invalid_input = True
        abacus_base = 0

choice = " "
while choice != "Q" and got_input:
    # Get number from user input to be displayed in the Abacus bar
    choice = get_abacus_number(abacus_base)

    # Check if user wants to quit mid-execution of program
    if choice == "Q":
        abort_message()
        break
    
    # Parse the user input to display into the Abacus bar    
    abacus_number = choice
    abacus_number = list(abacus_number)
    
    # Display the user input into the Abacus bar
    display_title_bar(abacus_base)
    display_abacus(abacus_number)

    # Terminate Program
    choice = "Q"
