# ---------------------------------------------------
# Title:     Professors Grading Tool
# Author:    Clint MacDonald
# Date:      March 14, 2025
# Purpose:   To demonstrate the use of functions in Python Application Development
# ---------------------------------------------------

#region IMPORTS
#endregion

#region CONSTANT DECLARATIONS
MAIN_MENU = '''Main Menu
-----------------
1. Enter a student grade
2. Find a student Grade
3. Calculate Class Average
4. Display All Marks
5. Exit
'''
#endregion

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

def getString(prompt: str):
    '''This function will get a string from the user''' 
    doContinue = True
    while doContinue:
        try:
            value = input(prompt)
            return value
        except ValueError as ve:
            print("Invalid input. Please enter a string.")

#endregion

#region APPLICATION FUNCTIONS
def initialize():
    print("Initializing")

def cleanup():
    print("Good-bye!")
    exit()

def enterGrade():
    '''This function will enter a student grade'''
    print('-'*40)
    student = getString("Enter student name: ")
    grade = getFloatRange("Enter student grade: ", 0.0, 100.0)
    students.append(student)
    grades.append(grade)
    print("Grade has been added.")
    print('-'*40)

def displayAllMarks():
    '''This function will display all student marks'''
    print('-'*40)
    print("Student Grades")
    print('-'*40)
    for i in range(len(students)):
        print("%-20s %.2f" % (students[i], grades[i]))
    print('-'*40)

def findGrade():
    '''This function will find a student grade'''
    print('-'*40)
    student = getString("Enter student name: ")
    if student in students:
        index = students.index(student)
        print("Student: %s has a grade of %.2f" % (student, grades[index]))
    else:
        print("Student not found.")
    print('-'*40)

def showClassAverage():
    '''This function will calculate the class average'''
    print('-'*40)
    total = sum(grades)
    try:
        average = total / len(grades)
        print("The class average is %.2f" % average)
    except ZeroDivisionError as zde:
        print("No students have been entered yet.")
    print('-'*40)

#endregion

#endregion

#region MAIN BODY

#region VARIABLE DECLARATIONS
students = []
grades = []
#endregion

initialize()

#region MENU

doContinue = True
while doContinue:
    # Display Menu
    print(MAIN_MENU)

    # Get User Choice
    choice = getIntegerRange("Enter your choice: ", 1, 5)

    # Process Choice
    if choice == 1:     enterGrade()        # Enter a student grade
    elif choice == 2:   findGrade()         # Find a student Grade
    elif choice == 3:   showClassAverage()  # Calculate Class Average
    elif choice == 4:   displayAllMarks()   # Display All Marks
    elif choice == 5:                       # Exit
        cleanup()
        doContinue = False

#endregion

#endregion