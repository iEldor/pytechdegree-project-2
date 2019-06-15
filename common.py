import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title(text):
    """takes a text as an input,
    surrounds with #, prints to console
    """
    print('#'*(len(text) + 6))
    print('##', text, '##')
    print('#'*(len(text) + 6))
    print()

    
def display_menu(message):
    """prints a message, takes user input,
    returns the user input
    """
    print(message)
    return input("Enter an option > ")


def invalid_entry(entry):
    """clears the screen, prints an invalid entry message"""
    clear_screen()
    print("\nWhoops! [{}] is an unexpected entry!\n".format(entry))
