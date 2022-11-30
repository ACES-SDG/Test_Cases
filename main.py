from tkinter import *
import os



root = Tk()

root.title('Tableau v0.0.1')
root.geometry('1200x600')
def DATA():
    print("DATA SOURCE")

def sheet():
    print("add any sheet")
def callback():
    filename = 'data.py'
    os.system(filename) #Open file [Same as Right-click Open]
def datasource():
    filename = 'datasource.py'
    os.system(filename)

bottomframe = Frame(root, borderwidth=6, bg="black", relief=GROOVE, width=370, height=2)
bottomframe.pack(side=BOTTOM, anchor=SE, fill=Y)
b1 = Button(bottomframe, fg="black", text="+",height=1, width=1)
b1.pack(side=RIGHT)
b1 = Button(bottomframe, fg="black", text="+",height=1, width=1)
b1.pack(side=RIGHT)
b1 = Button(bottomframe, fg="black", text="+")
b1.pack(side=RIGHT)
b1 = Button(bottomframe, fg="black", text="+")
b1.pack(side=RIGHT)


frame = Frame(root, borderwidth=6, bg="black", relief=SUNKEN, width=370, height=2)
frame.pack(side=BOTTOM, anchor=SW, fill=Y)
b1 = Button(frame, fg="black", text="DATASOURCE", command=datasource)
b1.pack(side=LEFT)

b2 = Button(frame, fg="black", text="Sheet", command=sheet)
b2.pack(side=LEFT)

b3 = Button(frame, fg="black", text="+")
b3.pack(side=LEFT)

b4 = Button(frame, fg="black", text="+")
b4.pack(side=LEFT)
b4 = Button(frame, fg="black", text="+")
b4.pack(side=LEFT)
upframe = Frame(root, borderwidth=6, bg="black", relief=SUNKEN)
upframe.pack(side=TOP, anchor=NW, fill=Y)
l = Label(upframe, font="Helvetica 16 bold", fg="red", pady=22)
l.pack()
b6 = Button(l, fg="black", text="menu", command=sheet)
b6.pack(side=LEFT, anchor=NW)
b7 = Button(l, fg="black", text="menu", command=sheet)
b7.pack(side=BOTTOM, anchor=NW)
sideframe = Frame(root, borderwidth=6, relief=SUNKEN)
sideframe.pack(side=LEFT, anchor=NW, fill=Y)
b4 = Menubutton(sideframe, fg="black", text="DATA")
b4.pack(side=LEFT, anchor=NW, padx=23)
b4.menu = Menu(b4, tearoff=0)
b4["menu"] = b4.menu
customer_name = IntVar()
location = IntVar()
order_date = IntVar()
order_id = IntVar()
product = IntVar()
b4.menu.add_checkbutton(label='costumers', variable=customer_name)
b4.menu.add_checkbutton(label='locations', variable=location)
b4.menu.add_checkbutton(label='order date', variable=order_date)
b4.menu.add_checkbutton(label='order id', variable=order_id)
b4.menu.add_checkbutton(label='product', variable=product)
b5 = Button(sideframe, fg="black", text="ANALYTICS", command=sheet)
b5.pack(side=LEFT, anchor=NW, padx=23)
sideframe1 = Frame(root, borderwidth=6, bg="black", relief=SUNKEN)
sideframe1.pack(side=LEFT, anchor=NW, fill=Y)
b4 = Button(sideframe1, fg="black", text="DATA SOURCE", command=DATA)
b4.pack(side=LEFT, anchor=NW)
b5 = Button(sideframe1, fg="black", text="ANALYTICS", command=sheet)
b5.pack(side=LEFT, anchor=NW)
sideframe2 = Frame(root, borderwidth=6, relief=SUNKEN, width=300, height=250)
sideframe2.pack(side=LEFT, anchor=NW, fill=Y)
b7 = Button(sideframe2, text="Browse", command=callback)
b7.pack(side=BOTTOM)
title_label = Label(sideframe2, text="DRAG     FILES    HERE", width=120, height=250)
title_label.pack()

sideframe3 = Frame(root, borderwidth=6, relief=SUNKEN, width=300, height=250)
sideframe3.pack(side=LEFT, anchor=SW, fill=Y)
title_label = Label(sideframe3, text="DRAG     FILES    HERE", width=37, height=250)
title_label.pack()

root.mainloop()






