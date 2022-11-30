from tkinter import *
from  tkinter import ttk
root = Tk()
root.geometry("200x100")
root.option_add("*TCombobox*Listbox*Background", "#1d2128")
root.option_add("*TCombobox*Listbox*Foreground", "#8b9ebf")
root.option_add("*TCombobox*Listbox*Font", "Courier")

style = ttk.Style()
style.theme_use("clam")
style.configure('TCombobox',
                         background="#1d2128",
                         fieldbackground="#1d2128",
                        
                         foreground="#8b9ebf",
                         darkcolor="lime",
                         selectbackground="grey",
                         lightcolor="lime"
                         )

opts = ["Hello", "Bye"]
cb = ttk.Combobox(root, values=opts)
cb.pack()

root.mainloop()