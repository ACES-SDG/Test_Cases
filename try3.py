from  tkinter.dnd import *
import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
import os
import matplotlib.pyplot as plt
from tkinter import filedialog as fd
import pandas as pd
import numpy as np
from try2 import graphs

my_file_path = []


def data_info(df):
    my_cols = df.columns
    my_rows = df.values
    print(df.info())
    print(my_file_path,'end ')
    # print(my_cols,'\n next')
    # print(my_rows)


def selectFile():
    #   if sheetpanel.winfo_exists():
    #      sheetpanel.pack()
    # if filepanel.winfo_exists():
    #    filepanel.pack()
    # if display_file.winfo_exists():
    #     display_file.pack()

    importf = fd.askopenfilename(initialdir="/", title="Select A File",
                                 filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    print(importf, 'importf')
    my_file_path.append(importf)
    # print(my_file_path, 'my_file_path')
    myfile()


def myfile():
    df = pd.read_excel(my_file_path[-1])
    print(df, 'df')
    print(my_file_path,'myfile')
    display_file.config(state='normal')
    display_file.insert('1.0', df)
    display_file.config(state='disabled')
    data_info(df)


def charts():
    sheetpanel.destroy()
    filepanel.destroy()
    display_file.destroy()
    print(my_file_path,'charts')
    print(my_file_path[-1],'charts-1')
    df = pd.read_excel(my_file_path[-1])
    graphs(root,df)

    pass
widg = []
def go():
    
    if sidepanel.winfo_ismapped():
        # for i in sidepanel.winfo_children():
        #     widg.append(i)
        sidepanel.pack_forget()
    else:
        sidepanel.pack(side=TOP)
        
        pass    
    
    pass

root = tk.Tk()
root.title("Ocean-Book1")

root.geometry("900x700")

oneframe = Frame(root, width=70, bg='white', relief=SUNKEN)
oneframe.pack_propagate(0)
oneframe.pack(side=LEFT, fill='y')

back = Frame(oneframe,width=70,bg='#52527a',height=50, relief=SUNKEN)
back.pack_propagate(0)
back.pack(side=TOP)


sidepanel = Frame(oneframe, width=70, bg='#52527a', height=750,relief=SUNKEN)
sidepanel.pack_propagate(0)
sidepanel.pack(side=TOP )

filepanel = Frame(root, height=450, width=1150)
filepanel.pack(side=BOTTOM, padx=70, anchor='sw', fill='x', expand=True)
filepanel.pack_propagate(0)


btn = Button(back,text=' <-- ',width=5,height=1,command=go)
btn.pack(side=TOP)

display_file = Text(filepanel)
display_file.config(state='disabled')
display_file.pack()

sheetpanel = Frame(root, width=200, bg='grey', height=40)
sheetpanel.pack_propagate(0)
sheetpanel.pack(side=TOP, fill='x', anchor='ne', padx=70)

AddIcon = PhotoImage(file="new_file.png")
inputBtn = Button(sidepanel, fg='#732626', bg='#52527a', text="import", image=AddIcon, command=selectFile)
inputBtn.pack(pady=50)

ChartsIcon = PhotoImage(file="charts.png")
sheetbtn = Button(sidepanel, fg='#732626', bg='#52527a', text="sheets", image=ChartsIcon, command=charts)
sheetbtn.pack()

root.mainloop()
