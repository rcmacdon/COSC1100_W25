# ----------------------------------------
# Title:  Menu Loop
# Author: Clint MacDonald
# Date:   Jan 24, 2025
# Purpose:  This program will display a menu of options to the user.  
#           The program will continue asking until the user chooses to
#           exit the broken.
# ------------------------------------------------

# greet the user and provide basic instructions
print("-"*60)
print("Welcome to the Menu Loop by Clint")
print("This program will display a menu of options to the user.")
print("-"*60)

# show the menu
menu = """MENU
------------------------------
1. Option 1
2. Option 2
3. Option 3
0. Exit
------------------------------"""

tryAgain = True
while tryAgain:
    # prompt the user, get the input, and store it in a temp variable
    choice = input(menu + "\n\nEnter your choice (0-3): ")

    # check if the user entered a valid choice
    if choice.isdigit():
        choice = int(choice)

        # check which option the user selected
        if choice == 0:
            tryAgain = False
        elif choice == 1:
            print("You selected Option 1")
        elif choice == 2:
            print("You selected Option 2")
        elif choice == 3:
            print("You selected Option 3")
        else:
            print("Invalid input. Please enter a number between 0 and 3.")
            continue
    else:
        print("Invalid input. Please enter a number between 0 and 3.")
        continue

print("Goodbye!")
exit()

