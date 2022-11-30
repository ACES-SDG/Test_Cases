from tkinter import BOTH, TOP, Canvas, Frame,  Tk, Label
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# from seaborn import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,  
    NavigationToolbar2Tk
)

df = pd. read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx")
# # Fixing random state for reproducibility
# np.random.seed(19680801)


N = 10
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
colors = np.random.choice(df['Sub-Category'], size=N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii
print(colors)


plt.scatter('Category', 'Sales',data=df, s='Profit', c=colors, alpha=0.5,sizes=(200,1500))
plt.show()



# root = Tk()

# fig = plt.figure('plot')
# leg_fig = plt.figure('legend')
# ax = fig.add_subplot(111)


# tips = sns.load_dataset("tips")
# print(tips.head())


# sns.scatterplot(
#     data=tips, x="total_bill", y="tip", hue="size", size="size",
#     sizes=(20, 200), hue_norm=(0, 7)
# )

# #  = sns.move_legend(ax,'center right')
# # ax.legend()
# legfig =leg_fig.legend(  bbox_to_anchor=(1.3, 0.6))
# canvas = FigureCanvasTkAgg(leg_fig,root)
# canvas.draw()
# canvas.get_tk_widget().pack(side=TOP,fill=BOTH,expand=1)
# # plt.scatter('Category', 'Sales',data=df)

# img = Frame(width=100,height=50,bg='yellow')
# img.pack(side= TOP)

# bard = Image.open()
# bardejov = ImageTk.PhotoImage()
# label1 = Label(img, image=legfig)
# label1.image = legfig
# label1.place(x=20, y=20)
# plt.show()


# sns.scatterplot(
#     data=df, x='Sub-Category', y="Sales", hue="Category", size="Profit",
#     sizes=(20, 200), 
# )
# # # sns.show()

# root.mainloop()