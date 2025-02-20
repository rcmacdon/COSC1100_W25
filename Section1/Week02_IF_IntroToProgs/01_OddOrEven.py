# -----------------------------------
# TITLE:    Week 2 - Odd or Even
# AUTHOR:   Clint MacDonald
# DATE:     Jan. 14, 2025
# PURPOSE:  Write a small program to receive a number from the user 
#           and determine if it is odd or even
# -----------------------------------

# greet the user
print("-----------------------------------")
print("Welcome to the Odd or Even program")

# get a input from the user and store it in a variable
userStr = input("Please enter a whole number: ")

# check if the input was a number
if userStr.isnumeric():      #userInt.isdigit():
    userInt = int(userStr)
    
# check if the number is even, else it is odd
    if userInt % 2 == 0:
        result = "even"
    else:
        result = "odd"

# output the result
    print("The number %i is %s" % (userInt, result))
else:
    print("You did not enter a whole number, good-bye")

print("-----------------------------------")