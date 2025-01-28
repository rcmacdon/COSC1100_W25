# -------------------------------------------
# TITLE:    IP2 Calculator with LOOP
# AUTHOR:   Clint MacDonald
# DATE:     Jan 24, 2025
# PURPOSE:  This program that calculates single digit integer math
# -------------------------------------------

# greet the user and provide basic instructions
print("-"*60)
print(
"""Welcome to the IP2 Calculator by Clint

This program will calculate single digit integer math.  
The user will input an integer followed by an operator (+, -, *, /) 
followed by another integer #O#.

example: 5*4 will do 5 x 4 = 20""")

print("-"*60)

tryAgain = True

while tryAgain:
    # prompt the user, get the input, and store it in a temp variable
    user_input = input("Enter your math problem (#O#, q to quit): ")

    if user_input.lower() == "q": 
        tryAgain = False
        continue

    # check if the length of the user input was 3
    elif len(user_input) != 3:
        print("Invalid input. Please enter single digit integers only.  Your entire input should be 3 characters long.")
        continue

    # split the user input into 3 separate variables
    num1 = user_input[0]
    operator = user_input[1]
    num2 = user_input[2]

    # convert the strings to integers
    if num1.isdigit() and num2.isdigit():
        num1 = int(num1)
        num2 = int(num2)

        # check which operator the user input and perform the appropriate math calculation

        if operator == "+":
            answer = num1 + num2
        elif operator == "-":
            answer = num1 - num2
        elif operator == "*":
            answer = num1 * num2
        elif operator == "/":
            # check if denominator is a 0
            if num2 == 0:
                print("Cannot divide by 0")
                continue
            else:
                answer = num1 / num2

        else: # the operator entered was not +, -, *, or /
            print("Invalid operator. Please enter +, -, *, or /")
            continue

        # print the answer
        print("%i %s %i = %f" % (num1, operator, num2, answer))

    else: # the user input was not single digit integers
        print("Invalid input. Please enter single digit integers only.")
        continue

print("Goodbye!")
print("-"*60)
exit()
