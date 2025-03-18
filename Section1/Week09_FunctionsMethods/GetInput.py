# ---------------------------------------------------
# Title:     An Example Application to show the use of functions
# Author:    Clint MacDonald
# Date:      March 13, 2025
# Purpose:   To demonstrate the use of functions in Python
# ---------------------------------------------------

#region IMPORT STATEMENTS
import math, random
#endregion IMPORT STATEMENTS


#region CONSTANT DECLARATION
GRAVITY = 9.81 # m/s^2
SHAPE_MENU = """Main Menu
--------------------
1. Circle
2. Rectangle
3. Square
4. Triangle
5. Quit
"""
#endregion CONSTANT DECLARATION


#region FUNCTION DEFINITIONS

#region USER INPUT FUNCTIONS

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
#endregion

#region SHAPE CALCULATION FUNCTIONS
def calculateCircle(radius: float):
    '''This function will calculate the area and perimeter of a circle'''
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    return area, perimeter

def calculateRectangle(length: float, width: float):
    '''This function will calculate the area and perimeter of a rectangle'''
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def calculateTriangle(base: float, height: float):
    '''This function will calculate the area and perimeter of a triangle'''
    area = 0.5 * base * height
    perimeter = base + 2 * math.sqrt(height**2 + base**2)
    return area, perimeter

#endregion

#region OUTPUT FUNCTIONS

def showOutput(shapeName: str, area: float, perimeter: float):
    '''This function will display the output to the user'''
    print("The area of the %s is %.2f \nThe perimeter of the %s is %.2f" % (shapeName, area, shapeName, perimeter))

#endregion

#endregion FUNCTION DEFINITIONS


#region MAIN APPLICATION

# Greet the user and show the main menu
print("Welcome to the Area and Perimeter Calculator")
print('-'*40)
print(SHAPE_MENU)

# Get the users choice
choice = getIntegerRange("Enter your choice (1-5): ", 1, 5)

print('-'*40)
# Process the users choice
if choice == 1:
    # Input
    radius = getFloat("Enter the radius of the circle: ")
    # Processing
    area, perimeter = calculateCircle(radius)
    # Output
    showOutput("circle", area, perimeter)

elif choice == 2:
    length = getFloat("Enter the length of the rectangle: ")
    width = getFloat("Enter the width of the rectangle: ")
    area, perimeter = calculateRectangle(length, width)
    showOutput("rectangle", area, perimeter)

elif choice == 3:
    side = getFloat("Enter the length of the side of the square: ")
    area, perimeter = calculateRectangle(side, side)
    showOutput("square", area, perimeter)

elif choice == 4:
    base = getFloat("Enter the base of the triangle: ")
    height = getFloat("Enter the height of the triangle: ")
    area, perimeter = calculateTriangle(base, height)
    showOutput("triangle", area, perimeter)

elif choice == 5:
    print("Goodbye")
    exit()

    # get user input ( INPUT )

    # do calculations ( PROCESSING )

    # output the results ( OUTPUT )
print('-'*40)

#endregion MAIN APPLICATION

