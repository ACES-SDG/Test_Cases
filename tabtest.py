
from tkinter import *
import tkinter as tk
from tkinter.ttk import Notebook

root = tk.Tk()
root.geometry('1200x600')

notebook = Notebook(root)
notebook.pack(fill=BOTH,expand=True)
def hello():
    print('hello')
    L = Label(root, text ="Right-click to display menu")
    L.pack()


tab1 = Frame(notebook,bg='blue')
tab2 = Frame(notebook,bg='red') 

# notebook.bind('<Button-3>',hello())



tab1.pack(fill=BOTH,expand=True)
tab2.pack(fill=BOTH,expand=True)

notebook.add(tab1,text='Blue Tab')
notebook.add(tab2,text='red Tab')

def func(tab):
    menu_icon_bar = Frame(tab, borderwidth=3, bg='#f9f9f9', relief=GROOVE,height=50,width=15)
    menu_icon_bar.pack_propagate(0)
    menu_icon_bar.pack(side=TOP, anchor="nw", fill=X)   


    sidepanel = Frame(tab,bg='black',width=400)
    sidepanel.pack(side=LEFT,fill=Y)

    box = Entry(tab,width=50)
    box.pack(side=TOP,fill=X)




root.mainloop()