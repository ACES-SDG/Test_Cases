import tkinter
from tkinter import *


root = Tk()
f1 = Frame(root,height=50,width=50).pack()

f2 = Frame(root, border=9,relief=SUNKEN,bg='red')
f2.pack()

L = Label(f2, text ="Right-click to display menu")
L.pack()

m = Menu(L, tearoff = 0)
m.add_command(label ="Cut")
m.add_command(label ="Copy")
m.add_command(label ="Paste")
m.add_command(label ="Reload")
m.add_separator()
m.add_command(label ="Rename")

def do_popup(event):
	try:
		m.tk_popup(event.x_root, event.y_root)
	finally:
		m.grab_release()

L.bind("<Button-3>", do_popup)

mainloop()
