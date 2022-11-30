from tkinter import *

root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT, fill="y", pady=122 )

f2= Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Ocean-DATA")
l.pack(pady=150)

l = Label(f2, text="welcome f2", font="Helvetica 16 bold", fg="red", padx=22)
l.pack()

root.mainloop()