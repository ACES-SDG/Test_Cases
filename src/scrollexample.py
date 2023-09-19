# Python program demonstrating
# ScrolledText widget in tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Creating tkinter main window
win = tk.Tk()
win.title("ScrolledText Widget")

# Title Label
ttk.Label(win,
		text = "ScrolledText Widget Example",
		font = ("Times New Roman", 15),
		background = 'green',
		foreground = "white").grid(column = 0,
									row = 0)

# Creating scrolled text
# area widget
text_area = scrolledtext.ScrolledText(win,
									wrap = tk.WORD,
									width = 40,
									height = 10,
									font = ("Times New Roman",
											15))

text_area.grid(column = 0, pady = 10, padx = 10)

text_area.insert(tk.INSERT,
"""\
This is a scrolledtext widget to make tkinter text read only.
Hi
Geeks !!!
Geeks !!!
Geeks !!! 
Geeks !!!
Geeks !!!
Geeks !!!
Geeks !!!
""")

# Placing cursor in the text area
text_area.focus()
win.mainloop()
