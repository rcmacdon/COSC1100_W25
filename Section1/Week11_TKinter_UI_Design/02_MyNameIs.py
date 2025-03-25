# ---------------------------------------------------
# Title:   Introduction to UI Controls and Events
# Author:  Clint MacDonald
# Date:    March 25, 2025
# Purpose: To demonstrate the basics of UI controls and Events and grid geometry
# ---------------------------------------------------

import tkinter as tk

def click_btnGo():
    lblOutput.config(text="Hello " + txtMyName.get())


window = tk.Tk()
window.title("My Name Is")
window.geometry("400x400")

lblTitle = tk.Label(window, text="Event Application", font=("Arial Bold", 20))
lblTitle.grid(row=0, column=0, columnspan=2)

lblMyName = tk.Label(window, text="My Name Is: ")
lblMyName.grid(row=1, column=0, sticky="E")

txtMyName = tk.Entry(window, width=20)
txtMyName.grid(row=1, column=1, sticky="W")

btnGo = tk.Button(window, text="Go", command=click_btnGo)
btnGo.grid(row=2, column=1, sticky="E")

lblOutput = tk.Label(window, text="", bg="lightgrey")
lblOutput.grid(row=3, column=0, columnspan=2, sticky="WE")

window.mainloop()