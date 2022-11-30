import tkinter as tk
import os

def callback():
    filename = 'data.py'
    os.system(filename) #Open file [Same as Right-click Open]
    os.system('notepad '+filename) #Open in notepad

root = tk.Tk()
tk.Button(root, text="Python File", command=callback).pack()
root.mainloop()