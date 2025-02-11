# --------------------------------
# Practice Exercises in prep for midterm
# --------------------------------

# Write a program that retrieves 2 numbers from the user and prints if the first number is divisible by the second number.

tryAgain = True

while tryAgain:
    try:
        # obtain input from user
        print("-"*30)
        print("Note: The following program works up to 2 decimal places only!")
        numerator = float(input("Please enter the Numerator: "))
        denominator = float(input("Please enter the Denominator: "))

        # check if the denominator is zero
        if denominator == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        
        # check if the numerator is divisible by the denominator
        # casting to an integer after multiplying by 100 to avoid floating point errors
        if round(int(numerator*100) % int(denominator*100),1) == 0.0:
            print("The numerator is divisible by the denominator")
        else:
            print("The numerator is not divisible by the denominator")

    except ZeroDivisionError as z:
        print(z)
    except Exception as e:
        print(e)

    #check if user wants to try again!
    tryAgain = input("Do you want to try again? (y/n)").lower() == "y"

# -- end of loop
print("Goodbye!")  
exit()

# --------------------------------
# Desk Check
# Test 1 - 10, 2    Expected Output: The numerator is divisible by the denominator 
#   Check: PASS
# Test 2 - 10, 3    Expected Output: The numerator is not divisible by the denominator 
#   Check: PASS
# Test 3 - 10, 0    Expected Output: Cannot divide by zero
#   Check: Pseudo PASS
# Test 4 - 3.9, 1.3 Expected Output: The numerator is divisible by the denominator
#   Check: FAIL because of floating point error
# Test 5 - 3.9, 1.2 Expected Output: The numerator is not divisible by the denominator
#   Check: FAIL because of floating point error
# Test 6 - 6, -2 Expected Output: The numerator is divisible by the denominator
#   Check: PASS
# Test 7 - -6, -2    Expected Output: The numerator is divisible by the denominator
#   Check: PASS
# Test 8 - 'Clint', 'dog' Expected Output: Invalid input
#   Check: Pseudo PASS







# Write a loop that prints even numbers between 50 and 10 backwards
    # use a for loop
    # use a while loop


# Write an if structure that determines if a number is positive, negative or zero



