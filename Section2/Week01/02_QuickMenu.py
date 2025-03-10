# --------------------------
# Title:    Menu Choice System
# Author:   Clint MacDonald, StudentID
# Date:     Jan 9, 2025
# Purpose:  This program allows the user to choose from 
#           a menu of what task they want to perform.
# --------------------------

# Print the menu to the console
print("Menu:")
print("-----------------")
print("1. Say Hello")
print("2. Say Hello World!")
print("3. Quit")

# Prompt the user for their choice and wait for the users response
choice = input("Enter a choice from 1 to 3?")

# Analyze the users response and perform the appropriate task
if choice == "1":
    name = input("What is your name? ")
    print("Hello, " + name + "!")
elif choice == "2":
    print("Hello, World!")
elif choice == "3":
    print("Goodbye!")
else:
    print("Invalid choice!")
# --------------------------
