from tkinter import *
import customtkinter as ctk
def hello():
    lbl = ctk.CTkLabel(a,text='Hello World, you clicked Button')
    lbl.pack()
    pass

a = Tk()
a.geometry('800x800')
a.minsize(700,700)

btn1 = ctk.CTkButton(a,width=50,text='Click me',command=hello).pack(anchor=CENTER)

a.mainloop()

