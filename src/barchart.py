from tkinter import *
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from packed_bubbles import BubbleChart
import random


df= pd.read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore2.xlsx")

colors_ = lambda n: list(map(lambda i: "#" + "%06x" % random.randint(0, 0xFFFFFF),range(n)))
x = len(df['City'].unique())
c_l=list(map(colors_,[x]))

df = df.groupby('City').agg({'Sales':sum})

root = Tk()

# fig, ax = plt.subplots(figsize =(7, 5))


bubble_chart = BubbleChart(area=list(df['Sales']),               
                           bubble_spacing=0)

bubble_chart.collapse()

fig, ax = plt.subplots()
bubble_chart.plot(
    ax,list(df.index),c_l[0]  )


ax.axis("off")
ax.relim()
ax.autoscale_view()
ax.set_title('Browser market share')

bar1 = FigureCanvasTkAgg(fig, root)
bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
# bar1.get_tk_widget().pack()

# frame = Frame()

root.mainloop()