# ---------------------------------------
# Title:    My Name Is Application
# Author:   Clint MacDonald
# Date:     March 25, 2025
# Purpose:  To create our first application using input controls
#           and demonstrating grid layout and events
# ---------------------------------------

import tkinter as tk
from tkinter import messagebox  # for message boxes
from idlelib.tooltip import Hovertip

# define the window
window = tk.Tk()
window.title("My Name Is")
window.geometry("400x200")

# define the event handlers
def btnGo_Click():
    name = txtName.get()
    lblOutput.config(text="Hello %s!" % name)

def escape_key():
    result = messagebox.askyesno("Quit", "Do you want to quit?")
    if result == True:  # if the user clicked 'OK'
        window.quit()

# add controls to the window
lblTitle = tk.Label(window, text="Welcome to 'My Name Is'", font=("Arial", 16))
lblTitle.grid(row=0, column=0, columnspan=2)

lblName = tk.Label(window, text="Enter your name:")
lblName.grid(row=1, column=0)

txtName = tk.Entry(window, width=20)
txtName.grid(row=1, column=1)

btnGo = tk.Button(window, text="Go", command=btnGo_Click)
btnGo.grid(row=2, column=1, sticky="e")

lblOutput = tk.Label(window, text="", bg="lightgrey")
lblOutput.grid(row=3, column=0, columnspan=2, sticky="ew")

# Tooltips
Hovertip(txtName, "Enter your name here")
Hovertip(btnGo, "Click to see your name")   

# Key Binds
window.bind("<Return>", lambda event: btnGo_Click())
window.bind("<Escape>", lambda event: escape_key())

# show the window
window.mainloop()