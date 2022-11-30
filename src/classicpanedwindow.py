import tkinter as tk
from tkinter import Label, ttk

root = tk.Tk()
root.title('PanedWindow Demo')
root.geometry('300x200')

# change style to classic (Windows only) 
# to show the sash and handle
# style = ttk.Style()
# style.theme_use('classic')

# paned window
pw = ttk.PanedWindow(orient=tk.HORIZONTAL)

# Left listbox
left_list = tk.Listbox(root)
left_list.pack(side=tk.LEFT)
pw.add(left_list)

# Right listbox
right_list = tk.Listbox(root)
right_list.pack(side=tk.LEFT)
pw.add(right_list)

# place the panedwindow on the root window
pw.pack(fill=tk.BOTH, expand=True)

right_listw = tk.Listbox(root)
right_listw.pack(side=tk.LEFT)
pw.add(right_listw)


l = Label(left_list, text= ' im checking the working of paned window from here to there')
l.pack()

root.mainloop()