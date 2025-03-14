# ---------------------------------------------------
# Title:     Continued Code for Application Planning Using Functions
# Author:    Clint MacDonald
# Date:      March 14, 2025
# Purpose:   To demonstrate the use of functions in Python Application Development
# ---------------------------------------------------

# Various Uses for Functions
'''
- Task Oriented Functions
- Helper Functions (smaller functions that help a larger function)
- Event Handler Functions
- Wrapper / WorkFlow Functions (functions that call other functions)
'''

''' example of some functions
def workflow():
    step1()
    step2()
    step3()

def step1():
    print("Step 1")

def step2():
    print("Step 2")

def step3():
    print("Step 3")
'''

''' ANOTHER EXAMPLE

def main():
    print("Welcome to the main function")
    initialize()
    runMenu()
    cleanup()
    exit()

def initialize():
    print("Initializing")

def runMenu():
    print("Running Menu")
    # show menu
    # get user choice
    # process choice
    if choice == 1:
        choice1()
    elif choice == 2:
        choice2()
    else:   # default choice
        defaultChoice()    
    
def choice1():
    print("Choice 1")

def choice2():
    print("Choice 2")

def defaultChoice():
    print("Default Choice")

def cleanup():
    print("Cleaning up")
'''

