import tkinter as tk
from tkhtmlview import HTMLLabel

root = tk.Tk()
html_label = HTMLLabel(root, html='<h1 style="color: blue;  text-align: center"> Hello World </h1>')
html_label.pack(fill="both", expand=True)
html_label.fit_height()
root.mainloop()