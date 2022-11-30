import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
import os
from tkinter import filedialog
import pandas as pd
import openpyxl

root = tk.Tk()
root.geometry("800x600")


def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    os.system(my_program)


def ask_qus():
    val = messagebox.askquestion("Exit?", "Do you want to exit?")
    if val == 'yes':
        root.destroy()


my_label = Label(root, text="")
my_label.pack()
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
data_menu = Menu(menubar)
server_menu = Menu(menubar)
help_menu = Menu(menubar)
# add a menu item to the menu

menubar.add_cascade(
    label="File",
    menu=file_menu
)
# add the File menu to the menubar

file_menu.add_command(
    label='New',
    command=''
)
file_menu.add_command(
    label='Open',
    command=open_program
)
file_menu.add_separator()
file_menu.add_command(
    label='Paste',
    command=''
)
file_menu.add_command(
    label='Exit',
    command=ask_qus
)
menubar.add_cascade(
    label="Data",
    menu=data_menu
)
data_menu.add_command(
    label='New Data Source',
    command=''
)
data_menu.add_separator()
data_menu.add_command(
    label='Refresh Data Source',
    command=''
)
data_menu.add_command(
    label='Duplicate Data Source',
    command=''
)
data_menu.add_command(
    label='Close Data Source',
    command=''
)
menubar.add_cascade(
    label="Server",
    menu=server_menu
)

menubar.add_cascade(
    label="Help",
    menu=help_menu
)

side_frame = Frame(root, bg='#355c80', width=300)
side_frame.pack(side=LEFT, fill='y', )

label1 = Label(side_frame, text='Connect', fg='white', font=('Times', 20))
label1.pack()
label2 = Label(side_frame, text='Search for Data')
label3 = Label(side_frame, text='Ocean Server')
label4 = Label(side_frame, text='')
label5 = Label(side_frame, text='To a File')

root.mainloop()
