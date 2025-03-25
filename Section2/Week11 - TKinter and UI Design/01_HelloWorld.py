# ---------------------------------------
# Title:    Hello World Application
# Author:   Clint MacDonald
# Date:     March 25, 2025
# Purpose:  To create our first application using TKinter in Python
# ---------------------------------------

# Import the TKinter library
import tkinter as tk

# Create the main window
myWindow = tk.Tk()
myWindow.title("Hello World Title")
myWindow.geometry("400x400")

# add a label to the window
lblHello = tk.Label(myWindow, text="Hello World", font=("Arial Bold", 20))
lblHello.pack()

# Start the main loop
myWindow.mainloop() 