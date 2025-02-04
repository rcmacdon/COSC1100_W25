# ----------------------------------
# Title: Data Types extended
# Author: Clint MacDonald
# Date: Feb. 4, 2025
# Purpose: To demonstrate the use of data types in Python
# ----------------------------------

# playing with data types
myInt = 5
myFloat = 5.0
myString = "Hello"

# print the data types
print(type(myInt))
print( type(myInt) == int )

print(type(myFloat))
print(type(myString))

# ------------------------------
# type checking

if (type(myInt) == int):
    print("myInt is an int")

if (type(myFloat) == float):
    print("myFloat is a float")

if (myInt == myFloat):
    print("myInt and myFloat are equal")

if (type(myInt) == type(myFloat)):
    print("myInt and myFloat are the same type")

str5 = "5"
if (type(myInt) == type(str5)):
    print("myInt and str5 are the same type")

if (myInt == str5):
    print("myInt and str5 are equal")

# ------------------------------
print(type(str5))

# check str5 can be converted to a number
if (str5.isnumeric()):
    print("str5 is a number")
    str5 = int(str5)

print(type(str5))

# type() is getType(), or typeOf() in C family of languages


# ----------------------------------
# Python ONLY: type checking
# ----------------------------------
# isinstance() is a Python specific function
# to check if a variable is of a certain type
if (isinstance(myInt, int)):
    print("myInt is an int")
# is the same as
if (type(myInt) == int):
    print("myInt is an int")