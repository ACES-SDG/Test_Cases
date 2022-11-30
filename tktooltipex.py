import tkinter as tk
import tkinter.ttk as ttk
from tktooltip import ToolTip

app = tk.Tk()
s = ttk.Style()
s.configure("custom.TButton", foreground="#ffffff", background="#1c1c1c")
b = tk.Button(app, text="Button", background='red',foreground='white')
b.pack()
ToolTip(b, msg="Hover info Hover info Hover info Hover info Hover info" , delay=0,
        parent_kwargs={"bg": "black", "padx": 5, "pady": 5},
        fg="#ffffff", bg="#1c1c1c", padx=10, pady=10)
app.mainloop()