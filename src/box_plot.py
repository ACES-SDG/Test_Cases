from tkinter import *
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,  
    NavigationToolbar2Tk
)
import pandas as pd

df = pd.read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx")

root= Tk()

fig, plot1 = plt.subplots(figsize =(7, 5))
y=df['Quantity']
x=df['Region']
sns.boxplot(x,y) #x = 'Region',
# plt.show()

# plot1.legend(loc='upper right')

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()

root.mainloop()