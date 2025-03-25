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
txtNum1 = tk.Entry(window, width=6)
txtNum2 = tk.Entry(window, width=6)
lblOutput = tk.Label(window, text="", bg="lightgrey")
#endregion

#region FUNCTIONS
def click_btnAdd():
    try:
        result = float(txtNum1.get()) + float(txtNum2.get())
        lblOutput.config(text="Result: " + str(result))
    except ValueError as ve:
        messagebox.showerror("Error", "Please enter only numbers")

def click_exit():
    response = messagebox.askyesno("Exit", "Do you want to exit the program?")
    if response == True:
        window.destroy()

#endregion

#region CREATE USER INTERFACE
def initialize_interface():
    window.title("My Addition Program")
    window.geometry("400x400")
    # Title Label
    lblTitle = tk.Label(window, text="Addition Application", font=("Arial Bold", 20), bg="lightgrey", border=2, relief="solid")
    lblTitle.grid(row=0, column=0, columnspan=4, sticky="WE")

    # Row 1 - Num1 + Num2 =
    txtNum1.grid(row=1, column=0, sticky="E")

    lblPlus = tk.Label(window, text="+")
    lblPlus.grid(row=1, column=1, sticky="WE")

    txtNum2.grid(row=1, column=2, sticky="W")

    btnAdd = tk.Button(window, text="=", command=click_btnAdd)
    btnAdd.grid(row=1, column=3, sticky="WE")

    # Row 2 - Output Label over 4 columns
    lblOutput.grid(row=2, column=0, columnspan=4, sticky="WE")

    # ToolTips
    Hovertip(txtNum1, "Enter the first number")
    Hovertip(txtNum2, "Enter the second number")
    Hovertip(btnAdd, "Click to add the numbers")

    # key binds
    window.bind("<Return>", lambda event:click_btnAdd())
    window.bind("<Escape>", lambda event:click_exit())
#endregion

#region MAIN
initialize_interface()
window.mainloop()
#endregion