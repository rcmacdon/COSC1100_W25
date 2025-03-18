# ------------------------------------------------------------------
# Title:       Tools to be used and available for many applications
# Date:        March 20, 2025
# Author:      Clint MacDonald
# ------------------------------------------------------------------

'''
Note that this file does use print statements in the functions meaning it is locked 
to the console.  If you want to use these functions in a GUI, you will need to modify the functions to return values instead of printing them.
'''

#region IMPORTS
import random, math
#endregion

#region USER INPUT FUNCTIONS

def get_string(prompt):
    '''Obtains a string from the user'''
    return input(prompt)

def get_string_length_range(prompt, min_length, max_length):
    '''Obtains a string from the user within a certain length range'''
    doContinue = True
    while doContinue:
        string = get_string(prompt)
        if len(string) >= min_length and len(string) <= max_length:
            return string
        else:
            print("Error: String must be between %i and %i characters long." % (min_length, max_length))

def getInteger(prompt: str):
    '''This function will get an integer from the user'''
    doContinue = True
    while doContinue:
        try:
            value = int(input(prompt))
            return value
        except ValueError as ve:
            print("Invalid input. Please enter a whole number.")

def getIntegerRange(prompt: str, minValue: int, maxValue: int):
    '''This function will get an integer from the user within a specified range'''
    doContinue = True
    while doContinue:
        try:
            value = int(input(prompt))
            if value < minValue or value > maxValue:
                raise ValueError
            else:
                return value
            return value
        except ValueError as ve:
            print("Invalid input. Please enter a whole number between %i and %i." % (minValue, maxValue))

def getFloat(prompt: str):
    '''This function will get an float from the user'''
    doContinue = True
    while doContinue:
        try:
            value = float(input(prompt))
            return value
        except ValueError as ve:
            print("Invalid input. Please enter a decimal number.")

def getFloatRange(prompt: str, minValue: float, maxValue: float):
    '''This function will get an float from the user within a range'''
    doContinue = True
    while doContinue:
        try:
            value = float(input(prompt))
            if value < minValue or value > maxValue:
                raise ValueError
            else:
                return value
        except ValueError as ve:
            print("Invalid input. Please enter a decimal number between %.2f and %.2f." % (minValue, maxValue))

#endregion

#region RANDOM NUMBER FUNCTIONS
# Function to return a Random Number
def get_random_integer(max_number):
    '''obtains a random integer between 1 and maximum number'''
    return random.randint(1, max_number)

# Function to return a Random Number (overloaded)
def get_random_integer_range(min_number, max_number):
    '''obtains a random integer between minimum number and maximum number'''
    return random.randint(min_number, max_number)

# Function to return a Random Float between 0 and 1
def get_random_float():
    '''obtains a random float between 0 and 1'''
    return random.random()

# Function to return a Random Float between 0 and 1 (overloaded)
def get_random_float(min_number, max_number):
    '''obtains a random float between minimum number and maximum number'''
    return random.uniform(min_number, max_number)

# Function to return a Random Element from a List
def get_random_element(list):
    '''obtains a random element from a list'''
    return random.choice(list)

# Function to return a Random Element List from a List (overloaded)
def get_random_element(list, number_of_elements):
    '''obtains a random list of elements from a list'''
    return random.sample(list, number_of_elements)
#endregion

#region SHAPE AREA FUNCTIONS
def calculateAreaCircle(radius: float):
    '''This function will calculate the area of a circle'''
    return math.pi * radius**2

def calculateAreaRectangle(length: float, width: float):
    '''This function will calculate the area of a rectangle'''
    return length * width

def calculateAreaTriangle(base: float, height: float):
    '''This function will calculate the area of a triangle'''
    return 0.5 * base * height
#endregion

#region SHAPE PERIMETER FUNCTIONS
def calculatePerimeterCircle(radius: float):
    '''This function will calculate the area and perimeter of a circle'''
    return 2 * math.pi * radius

def calculatePerimeterRectangle(length: float, width: float):
    '''This function will calculate the area and perimeter of a rectangle'''
    return 2 * (length + width)

def calculatePerimeterTriangle(base: float, height: float):
    '''This function will calculate the area and perimeter of a triangle'''
    return base + 2 * math.sqrt(height**2 + base**2)
#endregion