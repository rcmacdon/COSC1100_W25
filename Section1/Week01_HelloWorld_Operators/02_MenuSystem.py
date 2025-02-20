# ----------------------------------
# Title:    Menu System
# Author:   Clint MacDonald, StudentID
# Date:     January 9, 2025
# Purpose:  Prompt the user with a menu choice, process the choice, 
#           and execute the appropriate code.
# ----------------------------------

# Display the menu to the user.
print("----------------------------------")
print("Menu:")
print("----------------------------------")
print("1. Say Hello World!")
print("2. Say Who Am I")
print("3. Exit")

# Prompt the user for their choice and wait for the user to enter the data
choice = input("Enter your choice (1 - 3): ")

# Retrieve the user's choice from the variable 
# and execute the code of the user's choice.
if choice == "1":
    # Display the message "Hello, World!" to the user.
    print("Hello, World!")
elif choice == "2":               # else if
    # Prompt the user for their name and wait for the user to enter the data 
    # and store the value in a variable.
    name = input("What is your name? ")
    # Retrieve the user's name from the variable and display it to the user.
    print("Hello, " + name + "!")
elif choice == "3": 
    # Display the message "Goodbye!" to the user.
    print("Goodbye!")
else:
    # Display the message "Invalid Choice!" to the user.
    print("Invalid Choice!")

# end program
print("\n")