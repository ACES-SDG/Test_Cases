import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,  
    NavigationToolbar2Tk
)
from tkinter import *


# Setting size in Chart based on
# given values
# sizes = [100, 500, 70, 54, 440]

# # Setting labels for items in Chart
# labels = ['Apple', 'Banana', 'Mango', 'Grapes',
# 		'Orange']


# # explosion
# explode = (0.05, 0.05, 0.05, 0.05, 0.05)

# Pie Chart


# draw circle


# Displaying Chart
# plt.show()

df = pd.read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx")

data = df.groupby('Category').agg({'Sales':sum})
sizes = list(data['Sales'])
labels = list(data.index)

root= Tk()

fig, plot1 = plt.subplots(figsize =(7, 5))


plt.pie(sizes,  labels=labels,
		autopct='%1.1f%%', pctdistance=0.85,startangle = 90
		)

centre_circle = plt.Circle((0, 0), 0.60, fc='white')
fig = plt.gcf()

# Adding Circle in Pie chart
fig.gca().add_artist(centre_circle)

# Adding Title of chart
plt.title('Favourite Fruit Survey')

# Add Legends
plt.legend(labels, loc="upper right", title="Fruits Color")

canvas = FigureCanvasTkAgg(fig,master=root)
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()

# placing the canvas on the Tkinter window
canvas.get_tk_widget().pack()

root.mainloop()
