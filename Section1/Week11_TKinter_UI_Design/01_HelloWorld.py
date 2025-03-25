# ---------------------------------------------------
# Title:   Introduction to UI Design and TKinter
# Author:  Clint MacDonald
# Date:    March 25, 2025
# Purpose: To demonstrate the basics of UI design and TKinter
# ---------------------------------------------------

import tkinter as tk


window = tk.Tk()
window.title("Hello World Title")
window.geometry("400x400")

# Hungarian Notation
# the first 3-4 letters of the variable name are a prefix that indicates the type of the variable
lblString = tk.Label(window, text="Hello World")
lblString.pack()

window.mainloop()