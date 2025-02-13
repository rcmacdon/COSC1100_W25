# --------------------------------
# Practice Exercises in prep for midterm
# --------------------------------

# Practice Problem 1
# Write a program that retrieves 2 numbers from the user and prints if the 
# first number is divisible by the second number.
# Make sure the user can try a second time if either their input is invalid 
# or they complete it successfully.

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
        print("An error occurred: " + str(e))

    #check if user wants to try again!
    tryAgain = input("Do you want to try again? (y/n)").lower() == "y"

# -- end of loop

print("Goodbye!")  
exit()

# --------------------------------
# Desk Checks
# Test 1 - 10, 2    Expected Output: The numerator is divisible by the denominator
#   Check: PASS/FAIL
# Test 2 - 10, 3    Expected Output: The numerator is not divisible by the denominator
#   Check: PASS/FAIL
# Test 3 - 10, 0    Expected Output: Cannot divide by zero
#   Check: PASS/FAIL
# Test 4 - 3.9, 1.3 Expected Output: The numerator is divisible by the denominator
#   Check: PASS/FAIL
# Test 5 - 3.9, 1.2 Expected Output: The numerator is not divisible by the denominator
#   Check: PASS/FAIL
# Test 6 - 6, -2 Expected Output: The numerator is divisible by the denominator
#   Check: PASS/FAIL
# Test 7 - -6, -2    Expected Output: The numerator is divisible by the denominator
#   Check: PASS/FAIL
# Test 8 - 'Clint', 'dog' Expected Output: Invalid input
#   Check: PASS/FAIL





# Practice Problem 2
# Write a loop that prints even numbers between 50 and 10 backwards
    # use a for loop
    # use a while loop

print("-"*30)
for i in range(50, 9, -1):
    if i % 2 == 0:
        print(i)

print("-"*30)
for i in range(50, 9, -2):
        print(i)

print("-"*30)
i = 50
while i >= 10:
    if i % 2 == 0:
        print(i)
    i -= 1

# Practice Problem 3
# Write an if structure that prints if a number is positive, negative or zero
i = 45
if i > 0:
    print("The number is positive")
elif i < 0:
    print("The number is negative")
else:
    print("The number is zero")

# Practice Problem 4
# Write a program that prints the sum of all numbers between 1 and 100 that 
# are divisible by 3
# Hint: The answer is: 1683

sum = 0
for i in range(1, 101):
    if i % 3 == 0:
        sum += i
print("The sum of all numbers between 1 and 100 that are divisible by 3 is: %i" % sum)