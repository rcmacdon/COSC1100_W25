# -----------------------------------
# TITLE:    Week 3 - Our first Menu
# AUTHOR:   Clint MacDonald
# DATE:     Jan. 21, 2025
# PURPOSE:  Give options to the user for different actions
#           given user input
# -----------------------------------

# output the menu to the user
print("----------------------------------")
print("Menu:")
print("----------------------------------")
print("1. Say Hello World!")
print("2. Say Hello")
print("3. Calculate Fahrenheit from Celsius")
print("4. Exit")

# prompt the user for their choice
menu_choice = input("Enter your choice (1 - 4): ")

# validate the input to insure it is a number and within the range
if menu_choice.isdigit():
    # convert the input to an integer
    menu_choice = int(menu_choice[0])

    # check if number in the correct range
    if menu_choice >= 1 and menu_choice <= 4:
        # process the choice

        # determine which choice was made
        if menu_choice == 1:
            # say hello world
            print("Hello, World!")

        elif menu_choice == 2:
            # say hello
            print("Hello")

        elif menu_choice == 3:
            # calculate fahrenheit from celsius
            celsius = input("Enter the temperature in Celsius: ")

            





        elif menu_choice == 4:
            # exit the program
            print("Goodbye!")

        else:
            print("Invalid choice. Unknown Error.")

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

else:
    print("Invalid choice. Please enter a integer.")

