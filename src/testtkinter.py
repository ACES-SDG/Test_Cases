from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import matplotlib.pyplot as plt
from stackedBarmethod import stackedBar
# from packed_bubbles import BubbleChart
# color= ['#5A69AF', '#579E65', '#F9C784']
root  =Tk()
# fig, ax = plt.subplots(figsize =(7, 5))
# df = pd.read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx")

# bubble_chart = BubbleChart(area=df['Sales'],
#                            bubble_spacing=0)

# bubble_chart.collapse()

# bubble_chart.plot(
#     ax, df['Category'], color)
# ax.axis("off")
# ax.relim()
# ax.autoscale_view()


# fig = df.groupby(['Region','Sub-Category']).aggregate({'Sales':sum}).unstack(-2).plot(stacked=True, kind='bar')
# fig , ax= dfd.plot(stacked=True, kind='bar')
# plt.figure(figsize=(20,10))
# dfd[1].legend(loc=2)  
# plt.show()
# print(dfd, type(dfd))
# print(fig, type(fig))
fig = stackedBar()
bar1 = FigureCanvasTkAgg(fig, root)
bar1.get_tk_widget().pack(side=LEFT, fill=BOTH)
bar1.get_tk_widget().pack()

root.mainloop()