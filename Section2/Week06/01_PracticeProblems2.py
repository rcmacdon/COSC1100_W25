# ------------------------------------
# Practice Problems 2 
# Feb. 13, 2025
# ------------------------------------
# 1. Write a loop that adds up the numbers between a start number and an end number.  The numbers can be constants or input from the user.
START_NUMBER = 10
END_NUMBER = 35

total = 0
num = START_NUMBER
while num <= END_NUMBER:
    total += num
    num += 1
print("The sum of the numbers between %i and %i is %i" % (START_NUMBER, END_NUMBER, total))

# 2. Write a program that accepts two separate inputs from the user.  One being a road speed limit and one being the speed of a car.  If the car is speeding, print out a message to the user that they are speeding.  If they are not speeding, print out a message that they are not speeding.  If they are speeding, also print out the amount they are speeding by.  
# - The fine will be $10 per km over the limit
# - if they are 15 over the limit they will lose 3 demerit points from their license.  
# - if they are 30 over the limit they will lose 4 demerit points from their license.
# - if they are 45 over the limit they will lose 5 demerit points from their license.
# - if they are 50 over the limit they will lose 6 demerit points from their license, have their license suspended for 30 days and have their car impounded for 7 days.
tryAgain = True
while tryAgain:
    try:
        speedLimit = int(input("Enter the speed limit: "))
        carSpeed = int(input("Enter the speed of the car: "))
        if carSpeed > speedLimit:
            print("You are speeding by %i km/h" % (carSpeed - speedLimit))
            if carSpeed - speedLimit >= 50:
                print("You will lose 6 demerit points, have your license suspended for 30 days, and have your car impounded for 7 days.")
            elif carSpeed - speedLimit >= 45:
                print("You will lose 5 demerit points.")
            elif carSpeed - speedLimit >= 30:
                print("You will lose 4 demerit points.")
            elif carSpeed - speedLimit >= 15:
                print("You will lose 3 demerit points.")
            print("You will be fined $%i" % ((carSpeed - speedLimit) * 10))
        else:
            print("You are not speeding.")
        tryAgain = input("Would you like to try again? (y/n) ").lower() == "y"
    except ValueError as v:
        print("Please enter a valid number.")
# -- end of while loop
exit()

# 3. Write a program that calculates the factorial of a number.  The factorial of a number is the product of all the numbers from 1 to that number.  For example, the factorial of 5 is 5*4*3*2*1 = 120.  You do NOT need to use recursion for this problem.

tryAgain = true
while tryAgain:
    try:
        number = int(input("Enter a positive integer: "))
        if number < 0:
            print("Please enter a positive integer.")
        else:
            factorial = 1
            for i in range(1, number + 1):
                factorial *= i
            print("The factorial of %i is %i" % (number, factorial))
    except ValueError as v:
        print("Please enter a valid number.")

    tryAgain = input("Would you like to try again? (y/n) ").lower() == "y"
# -- end of while loop
exit()