# ---------------------------------------------------
# Title:   Practice Application to add 2 numbers
# Author:  Clint MacDonald
# Date:    March 25, 2025
# Purpose: To Practice what we previously learned
# ---------------------------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox, ttk
from idlelib.tooltip import Hovertip
#endregion

#region GLOBAL VARIABLES and CONSTANTS
window = tk.Tk()
num1 = tk.Entry(window, width=6)
num2 = tk.Entry(window, width=6)
lblOutput = tk.Label(window, text="", bg="lightgrey")
#endregion

#region FUNCTIONS
def click_btnAdd():
    try:
        result = int(num1.get()) + int(num2.get())
        lblOutput.config(text="Result: " + str(result))
    except ValueError as ve:
        messagebox.showerror("Error", "Please enter only numbers")
#endregion

#region CREATE USER INTERFACE
def initialize_interface():
    window.title("My Addition Program")

    
#endregion

#region MAIN

initialize_interface()
window.mainloop()

#endregion