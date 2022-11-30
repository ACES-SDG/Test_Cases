import plotly.graph_objects as go
from tkinter import *
import tkinter as tk

root = tk.Tk()

labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
fig.show()

root.mainloop()