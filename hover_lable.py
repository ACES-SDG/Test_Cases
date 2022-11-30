import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Hello, world", background="bisque", cursor="hand2")
label.pack(side="top", fill="x", padx=10, pady=10)

ok = tk.LabelFrame(root, text='label frame ', background='red', width=200,height=200 )
ok.pack(side='top')
root.mainloop()