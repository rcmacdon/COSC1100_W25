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

# Names for Functions
# -------------------
# Method - function used in a class definition (within an object)
# Function - function that returns a value (with a RETURN statement) )
# Sub-Routine - function that does not return anything
# Constructor - automatic function run when a new object is defined
# Getter or a Setter - manipulating properties of objects
# Accessor or a Mutator - same as getter and setter

# In this course we will only cover functions and sub-routines

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
# KEY IDEAS for designing Functions
# ---------------------------------------------------
# 1. Functions should be small and do ONE thing well
# 2. Functions should be reusable
# 3. Functions should be testable
# 4. Functions should not care WHY they are being used, they just do their job
# 5. Functions should be absolutely INDEPENDENT



# --------------------------------------------------- 
# Example simple Function

def sayHello():
    print("Hello World")


# at some time later in the code: Call the function
sayHello()

# Example2: Function with Parameters
def sayHelloTo(name):
    print("Hello " + name)

# Call the function with a parameter
myName = "Clint MacDonald"
sayHelloTo(myName)
sayHelloTo("Alice")
sayHelloTo("Bob")
# sayHelloTo()   # ERROR as parameter is required
# sayHello("Alice", "Bob")  # ERROR as only 1 parameter is expected
myInt = 4
# sayHelloTo(myInt)  # ERROR as the parameter is expected to be a string

# Example3: Function with Multiple Parameters
def sayHelloToV2(greeting: str, name: str):
    print(greeting + " " + name)

sayHelloToV2("Hello", "Alice")
sayHelloToV2("Goodbye", "Bob")  
sayHelloToV2("Where were you today", "Clint?")

# Example 4 - Mathematics
def add(a, b):
    return a + b

x = 4
y = 8
print(add(x, y))

answer = add(7, 2)
print(answer)

# Example 5 - Passing Parameters by Value
def calculateRaise(salary, raisePercent):
    newSalary = salary * (1 + raisePercent)
    salary = 0
    return newSalary

# application code
print('-'*40)
mySalary = 50000
myRaise = 0.05
print("Salary: %.2f   Raise: %.2f" % (mySalary, myRaise))
newSalary = calculateRaise(mySalary, myRaise)
print("Salary: %.2f   Raise: %.2f" % (mySalary, myRaise))
print("New Salary: %.2f" % newSalary)

# Example 6 - Returning Multiple Values
# PYTHON ONLY
def addAndSubtract(a: int, b: int):
    sum = a + b
    difference = a - b
    return sum, difference

# application code
print('-'*40)
x = 10
y = 4
sum, diff = addAndSubtract(x, y)
print("%i + %i = %i" % (x, y, sum))
print("%i - %i = %i" % (x, y, diff))