import tkinter as tk
import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
import os
from tkinter import filedialog
import pandas as pd
import openpyxl

def show_frame(frame):
    frame.tkraise()


window = tk.Tk()
window.state('zoomed')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')
# =============================Frame1 code====================================================
frame1_title = tk.Label(frame1, text='this is frame 1', bg='red')
frame1_title.pack(fill='x')

frame1_btn = tk.Button(frame1, text='enter', command=lambda: show_frame(frame2))
frame1_btn.pack()
# =============================Frame2 code====================================================

frame2_menubar = Menu(window)
window.config(menu=frame2_menubar)

# create a menu
file_menu = Menu(frame2_menubar)
help_menu = Menu(frame2_menubar)
# add a menu item to the menu


# add the File menu to the menubar
frame2_menubar.add_cascade(
    label="File",
    menu=file_menu
)
file_menu.add_command(
    label='New',
    command=''
)
file_menu.add_command(
    label='Open',
    command=""
)
file_menu.add_separator()
file_menu.add_command(
    label='Paste',
    command=''
)
file_menu.add_command(
    label='Exit',
    command=""
)
frame2_menubar.add_cascade(
    label="Data",
    menu=help_menu
)
help_menu.add_command(
    label='New Data Source',
    command=""
)
help_menu.add_separator()
help_menu.add_command(
    label='Refresh Data Source',
    command=''
)
help_menu.add_command(
    label='Duplicate Data Source',
    command=''
)
help_menu.add_command(
    label='Close Data Source',
    command=''
)
frame2_menubar.add_cascade(
    label="Server",
    menu=file_menu
)
frame2_menubar.add_cascade(
    label="Window",
    menu=file_menu
)
frame2_menubar.add_cascade(
    label="Help",
    menu=file_menu
)

show_frame(frame1)


window.mainloop()