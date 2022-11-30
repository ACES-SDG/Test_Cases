from tkinter import *
import tkinter as tk
from tkinter.simpledialog import askfloat
from tkinter.colorchooser import *

root = Tk()    

users = ['Anne','Bea','Chris']

a =IntVar()
for x in users:
    l = Checkbutton(root, text=x, variable=a,onvalue = 1,offvalue = 0)
    # print("l = Checkbutton(root, text=" + str(users[x][0]) + ", variable=" + str(users[x]))
    l.pack(anchor = 'w')
print(a.get())
root.mainloop()