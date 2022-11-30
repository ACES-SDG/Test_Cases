from tkinter import *
from tkinter import messagebox 


def top():
    
    if not any(isinstance(x, Toplevel) for x in root.winfo_children()):
            top = Toplevel(root)
            lbl = Label(top, text='TopLevel')
            lbl.pack()    
             
    else:
        
        messagebox.showinfo("showinfo", "Top level already exists")
        
    

root = Tk()

btn = Button(root, text='text', command=top)
btn.pack()

root.mainloop()
