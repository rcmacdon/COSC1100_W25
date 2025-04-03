# -------------------------------
# Title:    Listbox - one-to-many relationship choices
# Author:   Clint MacDonald
# Date:     April 3, 2025
# Purpose:  To work more with TKinter and some more interface choices
# -------------------------------

#region IMPORTS
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from idlelib.tooltip import Hovertip
#endregion

#region GLOBAL VARIABLES
window = tk.Tk()
lbxAvailable = tk.Listbox(window, selectmode=tk.MULTIPLE, height=15, width=20)
lbxSelected = tk.Listbox(window, selectmode=tk.MULTIPLE, height=15, width=20)
#endregion

#region FUNCTIONS

#region tools
def move_selected_items(source_listbox, target_listbox):
    '''Move selected items from source to target listbox'''
    selected_items = source_listbox.curselection()
    for index in selected_items[::-1]:  # Reverse to avoid index shifting
        item = source_listbox.get(index)
        target_listbox.insert(tk.END, item)
        source_listbox.delete(index)
    sort_listbox(target_listbox)

def move_all_items(source_listbox, target_listbox):
    '''Move all items from source to target listbox'''
    all_items = source_listbox.get(0, tk.END)
    for item in all_items:
        target_listbox.insert(tk.END, item)
    source_listbox.delete(0, tk.END)
    sort_listbox(target_listbox)

def sort_listbox(target_listbox):
    '''Sort the items in the selected listbox'''
    items = target_listbox.get(0, tk.END)
    sorted_items = sorted(items)
    target_listbox.delete(0, tk.END)
    for item in sorted_items:
        target_listbox.insert(tk.END, item)

#endregion

#region events
def btnExit_Click():
    '''Exit the program'''
    if messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?"):
        window.destroy()

def btnSelect_Click():
    '''Move selected items from available to selected listbox'''
    move_selected_items(lbxAvailable, lbxSelected)

def btnDeselect_Click():
    '''Move selected items from selected to available listbox'''
    move_selected_items(lbxSelected, lbxAvailable)

def btnSelectAll_Click():
    '''Move all items from available to selected listbox'''
    move_all_items(lbxAvailable, lbxSelected)

def btnDeselectAll_Click():
    '''Move all items from selected to available listbox'''
    move_all_items(lbxSelected, lbxAvailable)

#endregion

#endregion

#region interface
def create_ui():
    '''Create the main window and all widgets'''
    window.title("Listbox Fun")
    window.geometry("345x310")
    window.resizable(False, False)

    # row 0
    # column 0
    lbxAvailable.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

    # column 1
    btnSelectAll = tk.Button(window, text=">>", width=5, command=btnSelectAll_Click)
    btnSelectAll.grid(row=0, column=1, padx=5, pady=5)
    Hovertip(btnSelectAll, "Move all items to the right")

    # column 2
    lbxSelected.grid(row=0, column=2, rowspan=4, padx=10, pady=10)

    # row 1
    # column 1
    btnSelect = tk.Button(window, text=">", width=5, command=btnSelect_Click)
    btnSelect.grid(row=1, column=1, padx=5, pady=5)
    Hovertip(btnSelect, "Move Selected items to the right")

    # row 2
    # column 1
    btnDeselect = tk.Button(window, text="<", width=5, command=btnDeselect_Click)
    btnDeselect.grid(row=2, column=1, padx=5, pady=5)   
    Hovertip(btnDeselect, "Move Selected items to the left")

    # row 3
    # column 1
    btnDeselectAll = tk.Button(window, text="<<", width=5, command=btnDeselectAll_Click)
    btnDeselectAll.grid(row=3, column=1, padx=5, pady=5)
    Hovertip(btnDeselectAll, "Move all items to the left")

    # row 4
    # column 0
    btnExit = tk.Button(window, text="Exit", width=7, command=btnExit_Click)
    btnExit.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="e")
    Hovertip(btnExit, "Exit the program")

def load_data():
    '''Load the data into the listboxes'''
    # Load available items
    available_items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
    for item in available_items:
        lbxAvailable.insert(tk.END, item)

#endregion

#region main
create_ui()
load_data()
window.mainloop()
exit()
#endregion