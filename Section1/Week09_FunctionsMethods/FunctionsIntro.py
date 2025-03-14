# ---------------------------------------------------
# Title:     Introduction to Functions in Programming
# Author:    Clint MacDonald
# Date:      March 13, 2025
# Purpose:   To demonstrate the use of functions in Python
# ---------------------------------------------------

# Functions are a way to group code together and give it a name. This allows you to reuse the code multiple times without having to write it out each time. Functions can also take in input PARAMETERS and RETURN output. This allows you to create more flexible and reusable code.

# ---------------------------------------------------
# Verbage of Functions
# ---------------------------------------------------

# Various Names used for Functions:
# - Function
# - Method
# - Procedure
# - Subroutine
# - Constructor
# - Destructor
# - Getter or Setter
# - Accessor or Mutator
# - Lambda or Anonymous Function (arrow notation)

# in this course we will cover only functions and sub-routines

# ---------------------------------------------------
# Basic Rules of Functions
# ---------------------------------------------------
# 1. Function names should be descriptive and meaningful usually starting with a verb.
# 2. In Python, functions are declared separately from where they are called and using the "def" keyword
# 3. In Python, functions are declared BEFORE they are used.
# 4. Functions are called using the name and parenthesis ().
# 5. Functions can take in PARAMETERS which are values passed into the function.
# 6. Parameters may have default values
# 7. Functions can RETURN a value using the "return" keyword.
# 8. Functions can have multiple return statements but only one will be executed
# ---------------------------------------------------

# ---------------------------------------------------
# KEY IDEAS for designing functions
# ---------------------------------------------------
# 1. Functions should be small and do ONE thing well (PERFECT)
# 2. Functions should be reusable
# 3. Functions should be testable
# 4. Functions should not care WHY they are being used, they just do their job
# 5. Functions should be absolutely INDEPENDENT of other functions

# ---------------------------------------------------
# Example simple Function

def sayHello():
    '''A Function that prints out Hello World'''
    print("Hello World!")
# end of sayHello() function

# ---------------------------------------------------
# Calling the Function
sayHello()
# ---------------------------------------------------

# Example 2
def sayHelloTo(name):
    '''A Function that prints out Hello to a specific person'''
    print("Hello %s!" % name)

# ---------------------------------------------------
# Calling the Function
sayHelloTo("John")
myName = "Clint"
sayHelloTo(myName)
sayHelloTo("Sue")
# sayHelloTo()    # ERROR - no parameter was provided
# sayHelloTo("Bob", "Alice")  # ERROR - too many parameters
myInt = 4
sayHelloTo(myInt)  # No Error - Python is dynamically typed

# Example 3
def sayHelloToV2(greeting: str, name: str):
    '''A Function that prints out a custom greeting to a specific person'''
    print("%s %s!" % (greeting, name))

# ---------------------------------------------------
# Calling the Function
sayHelloToV2("Good Morning", "John")
sayHelloToV2("Good Afternoon", "Sue")
sayHelloToV2("Why were you not in class today", "Bob?")

# Example 4 - Mathematics
def addTwoNumbers(num1, num2):
    '''A Function that adds two numbers together'''
    return num1 + num2

# ---------------------------------------------------
# Calling the Function
sum = addTwoNumbers(5, 7)
print(sum)
print(addTwoNumbers(3, 4))
# ---------------------------------------------------

# Example 5 - Passing Parameters by Value
def calculateRaise(salary: float, raisePercent: float):
    '''A Function that calculates a raise based on a percentage'''
    newSalary = salary * (1 + raisePercent)
    salary = 0 # has no impact on MySalary below because it is passed "by value"
    return newSalary

# ---------------------------------------------------
# Calling the Function
mySalary = 50000
myRaise = 0.05
print("My salary is: $%.2f and my raise is %.2f" % (mySalary, myRaise))
newAmount = calculateRaise(mySalary, myRaise)
print("My salary is: $%.2f and my raise is %.2f" % (mySalary, myRaise))
print("My new salary is: $%.2f" % newAmount)

# Example 6 - returning multiple values
# PYTHON ONLY
def addAndSubtract(a: int, b: int):
    '''A Function that adds and subtracts two numbers'''
    add = a + b
    sub = a - b
    return add, sub

# ---------------------------------------------------
# Calling the Function
sum, diff = addAndSubtract(10, 5)
print("Sum: %d, Diff: %d" % (sum, diff))