# ----------------------------------
# Title: Dice Rolling
# Author: Clint MacDonald
# Date: March 27, 2025
# Purpose: Another example to work from in TKinter!
# ----------------------------------

#region Imports
import tkinter as tk
from tkinter import messagebox  # for message boxes
from tkinter import ttk  # for combobox
from idlelib.tooltip import Hovertip
import random
#endregion

#region Global Variables

# Interactive Form Controls
window = tk.Tk()
txtNumDice = tk.Entry(window, width=9)
cboNumSides = ttk.Combobox(window, width=6)
lbxResults = tk.Listbox(window, width=30, height=15)

#endregion

#region Functions

# Initialize Interface
def initialize_interface():
    '''This function initializes the interface'''
    # Set the window title
    window.title("Dice Rolling Tool")
    window.geometry("400x400")

    # create and setup properties of the other controls
    lblTitle = tk.Label(window, text="Dice Rolling Tool", font=("Arial", 16))
    lblTitle.grid(row=0, column=0, columnspan=3)

    # Row 1 
    lblNumDice = tk.Label(window, text="Number of Dice:")
    lblNumDice.grid(row=1, column=0, sticky="e")

    txtNumDice.grid(row=1, column=1, sticky="w")

    lbxResults.grid(row=1, column=2, rowspan=3, sticky="nsew")

    # Row 2
    lblNumSides = tk.Label(window, text="Number of Sides:")
    lblNumSides.grid(row=2, column=0, sticky="e")

    cboNumSides.grid(row=2, column=1, sticky="w")
    cboNumSides['values'] = (4, 6, 8, 10, 12, 20)

    # Row 3
    btnRoll = tk.Button(window, text="Roll Dice", command=btnRoll_Click)
    btnRoll.grid(row=3, column=0, columnspan=2, sticky="e", padx=10)

    # Row 4
    btnClear = tk.Button(window, text="Clear Results", command=btnClear_Click)
    btnClear.grid(row=4, column=1, sticky="e", pady=10)

    btnExit = tk.Button(window, text="Exit", command=btnExit_Click)
    btnExit.grid(row=4, column=2, sticky="e", pady=10)

    # key binds
    window.bind("<Return>", lambda event: btnRoll_Click())
    window.bind("<Escape>", lambda event: btnExit_Click())
    window.bind("<Alt-c>", lambda event: btnClear_Click())

    # tooltips
    Hovertip(txtNumDice, "Enter the number of dice to roll")
    Hovertip(cboNumSides, "Select the number of sides on the dice")
    Hovertip(btnRoll, "Click to roll the dice")
    Hovertip(btnClear, "Click to clear the results")
    Hovertip(btnExit, "Click to exit the program")

# event for the roll button click
def btnRoll_Click():
    '''This function rolls the dice'''
    # validate data
    if isValid():
    
        # retrieve the numDice and numSides values
        numDice = int(txtNumDice.get())
        numSides = int(cboNumSides.get())
        results = []
            
        # roll the dice
        for i in range(numDice):
            roll = random.randint(1, numSides)
            results.append(roll)
        
        # add the result to the listbox
        lbxResults.insert(0, results)
        
def btnClear_Click():
    '''This function clears the results'''
    lbxResults.delete(0, tk.END)

    # clear the listbox

def btnExit_Click():
    '''This function exits the program'''
    if messagebox.askyesno("Exit Confirmation", "Do you want to exit?"):
        window.destroy()

def isValid():
    '''This function validates the data'''
    try:
        numDice = int(txtNumDice.get())
        numSides = int(cboNumSides.get())
        return True
    except ValueError as ve:
        messagebox.showerror("Invalid Input", "Please enter a valid number of dice and sides")
        return False

def main():
    '''This function runs the main program'''
    initialize_interface()
    window.mainloop()
#endregion

#region Main

# Initialize the Interface
main()
# Exit program
exit()

#endregion