from  matplotlib.widgets import LassoSelector
import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore2.xlsx")
x=df['Category']
y=df['Sales']

ax = plt.subplot()
ax.plot(x, y)

def onselect(verts):
    print(verts)
lasso = LassoSelector(ax, onselect)