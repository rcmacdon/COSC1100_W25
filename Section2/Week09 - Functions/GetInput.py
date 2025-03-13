# ---------------------------------------------------
# Title:     First Application Using Function
# Author:    Clint MacDonald
# Date:      March 13, 2025
# Purpose:   To demonstrate the use of functions in Python
# ---------------------------------------------------

#region IMPORTS
import math, random
#endregion IMPORTS

#region CONSTANT DECLARATIONS
GRAVITY = 9.81 # m/s^2
F_TO_C_RATIO = 5/9
C_TO_F_RATIO = 9/5

SHAPE_MENU = """Main Menu
-----------------
1. Circle
2. Rectangle
3. Square
4. Triangle
5. Exit
"""
#endregion CONSTANT DECLARATIONS

#region FUNCTION DEFINITIONS

#region INPUT FUNCTIONS
# Function to get an integer from the user
def getInteger(prompt):
   '''Function to get an integer from the user '''
   tryAgain = True
   while tryAgain:
      try:
         return int(input(prompt))
      except ValueError as ve:
         print("Please enter an integer value!")
# ----- end of getInteger function

def getIntegerRange(prompt: str, minVal: int, maxVal: int):
   '''Function to get an integer from the user '''
   tryAgain = True
   while tryAgain:
      try:
         userInput = int(input(prompt))
         if userInput >= minVal and userInput <= maxVal:
            return userInput
         else:
            raise ValueError
      except ValueError as ve:
         print("Please enter an integer value between %i and %i!" % (minVal, maxVal))
# ----- end of getInteger function

# Function to get an float from the user
def getFloat(prompt):
   '''Function to get an float from the user '''
   tryAgain = True
   while tryAgain:
      try:
         return float(input(prompt))
      except ValueError as ve:
         print("Please enter an float value!")
# ----- end of getInteger function

#endregion INPUT FUNCTIONS

#region SHAPE CALCULATIONS

def calculateCircle(radius: float):
    '''Function to calculate the area and perimeter of a circle'''
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

def calculateRectangle(width: float, length: float):
    '''Function to calculate the area and perimeter of a rectangle'''
    area = width * length
    perimeter = 2 * (width + length)    
    return area, perimeter

#endregion SHAPE CALCULATIONS

#region OUTPUT FUNCTIONS

def outputResults(shape: str, area: float, perimeter: float):
    '''Function to output the results of the shape calculations'''
    print("%s Area: %.3f\n%s Perimeter: %.3f" % (shape, area, shape, perimeter))

#endregion OUTPUT FUNCTIONS  

#endregion FUNCTION DEFINITIONS

#region MAIN APPLICATION

print('-'*40)
print("Welcome to the Area and Perimeter Calculator")
print(SHAPE_MENU)
choice = getIntegerRange("Please enter your choice (1-5): ", 1, 5)

# process choice

if choice == 1:
    print("-"*40)
    radius = getFloat("Please enter the circle radius: ")
    area, perimeter = calculateCircle(radius)
    outputResults("Circle", area, perimeter)
    input("Please hit enter to continue...")

elif choice == 2:   
    print('-'*40)
    width = getFloat("Please enter the rectangle width: ")
    length = getFloat("Please enter the rectangle length: ")
    area, perimeter = calculateRectangle(width, length)
    outputResults("Rectangle", area, perimeter)
    input("Please hit enter to continue...")

elif choice == 3:
    print('-'*40)
    side = getFloat("Please enter the square side length: ")
    area, perimeter = calculateRectangle(side, side)
    outputResults("Square", area, perimeter)
    input("Please hit enter to continue...")

elif choice == 4:
    print("Triangle")
else:
    print("Goodbye!")
# end of if


#endregion  MAIN APPLICATION

# ---------------------------------------------------