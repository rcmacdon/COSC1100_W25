# ---------------------------------------
# Title:    My Name Is Application
# Author:   Clint MacDonald
# Date:     March 25, 2025
# Purpose:  To create our first application using input controls
#           and demonstrating grid layout and events
# ---------------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox  # for message boxes
from idlelib.tooltip import Hovertip
#endregion

#region GLOBAL VARIABLES AND CONSTANTS
window = tk.Tk()
txtNum1 = tk.Entry(window, width=6)
txtNum2 = tk.Entry(window, width=6)
lblOutput = tk.Label(window, text="", bg="lightgrey")
#endregion

#region Functions and Events

#region Creating the User Interface
def initialize_interface():
    window.title("My Addition Tool")
    window.geometry("400x200")

    # Row 0 - Title Row
    lblTitle = tk.Label(window, text="Welcome to 'My Addition Tool'", font=("Arial", 16))
    lblTitle.grid(row=0, column=0, columnspan=4)

    # Row 1 - Num1 + Num2 =
    txtNum1.grid(row=1, column=0, sticky="e")

    lblPlus = tk.Label(window, text="+")
    lblPlus.grid(row=1, column=1, sticky="ew")

    txtNum2.grid(row=1, column=2, sticky="w")

    btnEquals = tk.Button(window, text="=", command=btnEquals_Click)
    btnEquals.grid(row=1, column=3, sticky="e")

    # Row 2 - Output
    lblOutput.grid(row=2, column=0, columnspan=4, sticky="ew")

    # ToolTips
    Hovertip(txtNum1, "Enter the first number")
    Hovertip(txtNum2, "Enter the second number")
    Hovertip(btnEquals, "Click to see the sum")

    # Key Binds
    window.bind("<Return>", lambda event: btnEquals_Click())
    window.bind("<Escape>", lambda event: escape_key())

#endregion

#region Event Handlers
def btnEquals_Click():
    try:
        num1 = float(txtNum1.get())
        num2 = float(txtNum2.get())
        result = num1 + num2
        lblOutput.config(text="The sum is %.3f" % result)
    except ValueError as ve:
        messagebox.showerror("Error", "Please enter valid numbers")
    except Exception as e:
        messagebox.showerror("Error", "An error occurred: %s" % e)

def escape_key():
    result = messagebox.askyesno("Quit", "Do you want to quit?")
    if result == True:  # if the user clicked 'OK'
        window.quit()
#endregion

#endregion



#region MAIN
initialize_interface()
window.mainloop()
#endregion

