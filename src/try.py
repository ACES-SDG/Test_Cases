import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
import os
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
import pandas as pd
from try2 import graphs

import numpy as np

root = tk.Tk()
root.title("Ocean-Book1")

root.geometry("900x700")

sidepanel = Frame(root, width=70, bg='#3385ff', relief=SUNKEN)
sidepanel.pack_propagate(0)
sidepanel.pack(side=LEFT, fill='y')

my_file_path = []


def selectFile():
    importf = fd.askopenfilename(initialdir="/", title="Select A File",
                                 filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    print(importf, 'importf')
    my_file_path.append(importf)
    print(my_file_path, 'my_file_path')
    myfile()


filepanel = Frame(root, height=450, width=1150)
filepanel.pack(side=BOTTOM, padx=70, anchor='sw', fill='x', expand=True)
filepanel.pack_propagate(0)

display_file = Text(filepanel)
display_file.config(state='disabled')
display_file.pack()


def myfile():
    try:
        if my_file_path[-4:] == ".csv":
            df = pd.read_csv(my_file_path[-1])

        else:
            df = pd.read_excel(my_file_path[-1])

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {my_file_path}")
        return None
    #    df = pd.read_excel(my_file_path[-1])
    print(df, 'df')
    display_file.config(state='normal')
    display_file.insert('1.0', df)
    display_file.config(state='disabled')
    data_info(df)


sheetpanel = Frame(root, width=100, bg='yellow', height=40)
sheetpanel.pack_propagate(0)
sheetpanel.pack(side=TOP, fill='x', anchor='ne', padx=70)

AddIcon = PhotoImage(file="C:/Users/acesi/PycharmProjects/Ocean25/new_file.png")

inputBtn = Button(sidepanel, fg='#732626', bg='#3385ff', text="import", image=AddIcon, command=selectFile)
inputBtn.pack(pady=50)


sheetbtn = Button(sheetpanel, fg='red', bg='black', text='addSheet', command=charts())
sheetbtn.pack_propagate(0)
sheetbtn.place(x=20, y=5)
sheetbtn.pack(padx=20, side=LEFT)

def charts():
    sidepanel.destroy()
    inputBtn.destroy()
    sheetpanel.destroy()
    sheetbtn.destroy()
    filepanel.destroy()
    display_file.destroy()
    df = pd.read_excel(my_file_path[-1])
    graphs(root, df)
    pass
def data_info(df):
    my_cols = df.columns
    my_rows = df.values
    print(df.info())
    # print(my_cols,'\n next')
    # print(my_rows)





root.mainloop()
