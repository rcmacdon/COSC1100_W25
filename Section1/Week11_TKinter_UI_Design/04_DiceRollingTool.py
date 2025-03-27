# -------------------------------
# Title: Dice Rolling Tool
# Author: Clint MacDonald
# Date: March 27, 2025
# Purpose: To work more with TKinter and application architecture
# -------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip
import random
#endregion

#region GLOBAL VARIABLES
window = tk.Tk()
txtNumDice = tk.Entry(window, width=9)
cboNumSides = ttk.Combobox(window, width=6)
lbxResults = tk.Listbox(window, width=15, height=12)
#endregion

#region FUNCTIONS

#region interface

    # Initialize Controls
def initialize_controls():
    '''This function will create and place all the controls on the window'''
    window.title("Dice Rolling Tool")

    # Row 0
    lblTitle = tk.Label(window, text="Dice Rolling Tool", font=("Arial", 16), anchor="center")
    lblTitle.grid(row=0, column=0, columnspan=3)

    # Row 1
    lblNumDice = tk.Label(window, text="Number of Dice:")
    lblNumDice.grid(row=1, column=0, sticky="e")

    txtNumDice.grid(row=1, column=1, sticky="w")

    lbxResults.grid(row=1, column=2, rowspan=3, padx=10, sticky="nsew")

    # Row 2
    lblNumSides = tk.Label(window, text="Number of Sides:")
    lblNumSides.grid(row=2, column=0, sticky="e")   

    cboNumSides.grid(row=2, column=1, sticky="w")
    cboNumSides['values'] = (4, 6, 8, 10, 12, 20)

    # Row 3
    btnRoll = tk.Button(window, text="Roll", width=10, command=btnRoll_click)
    btnRoll.grid(row=3, column=1, padx=10, sticky="e")

    # Row 4
    btnClear = tk.Button(window, text="Clear", width=10, command=btnClear_click)
    btnClear.grid(row=4, column=1, padx=10, sticky="e")

    btnExit = tk.Button(window, text="Exit", width=10, command=btnExit_click)
    btnExit.grid(row=4, column=2, pady=10, padx=10, sticky="e")

    # Key Bindings
    window.bind("<Return>", lambda event: btnRoll_click())
    window.bind("<Escape>", lambda event: btnExit_click())
    window.bind("<Alt-c>", lambda event: btnClear_click())

    # Tooltips
    Hovertip(txtNumDice, "Enter the number of dice to roll.")
    Hovertip(cboNumSides, "Select the number of sides for the dice.")
    Hovertip(btnRoll, "Click to roll the dice.")
    Hovertip(btnClear, "Click to clear the results.")
    Hovertip(btnExit, "Click to exit the application.")
    Hovertip(lbxResults, "Results of the dice rolls.")

def btnRoll_click():
    '''This function will roll the dice and display the results in the listbox'''

    # Validate the input values
    if isValid():
        # Get the number of dice and number of sides
        numDice = int(txtNumDice.get())
        numSides = int(cboNumSides.get())
        results = []

        # Roll the dice and add the results to the listbox
        for i in range(numDice):
            roll = random.randint(1, numSides)
            results.append(roll)
        
        # add the dice roll(s) to the listbox 
        lbxResults.insert(0, results)

    # Clear button click event
def btnClear_click():
    '''This function will clear the listbox of all items'''
    lbxResults.delete(0, tk.END)

    # Exit button click event
def btnExit_click():
    '''This function will confirm the user wants to exit the application and then close the window'''
    if messagebox.askyesno("Exit Application", "Are you sure you want to exit?"):
        window.destroy()

#endregion

#region logic
    # main function
def main():
    initialize_controls()
    window.mainloop()

    # roll dice function

    # validate input values
def isValid():
    '''This function will validate the input values for the number of dice and number of sides'''
    try:
        numDice = int(txtNumDice.get())
        numSides = int(cboNumSides.get())

        if numDice < 1 or numDice > 8:
            raise ValueError("Number of dice must be between 1 and 8.")
        
        return True
    except ValueError as ve:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for the number of dice and number of sides.")
        return False

    # clear results function
#endregion

#endregion

#region MAIN APPLICATION
main()
exit()
#endregion
