
import matplotlib.pyplot as plt
import pandas as pd

# Define Data

df = pd.DataFrame(dict(
    x1=[3, 4, 5, 6],
    x2=[5, 9, 11.2, 14],
    x3=[1.6, 3, 4, 6.5],
    x4=[4.5, 5.5, 8.9, 12]))

# Stacked grouped bar chart

plt.bar(['a','b','c','d'], df.x2, align='edge', width= 0.4,color='g')
plt.bar(['a','b','c','d'], df.x1, align='edge', width= 0.4,color='c')
plt.bar(['a','b','c','d'], df.x4, align='edge',width= -0.4, color='r')
# plt.bar([0, 1, 2, 3], df.x3, align='edge',width= -0.4,color='y')

plt.axis(False)
# Show

plt.show()