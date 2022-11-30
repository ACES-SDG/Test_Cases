import matplotlib.pyplot as plt
import pandas as pd

df = pd. read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore.xlsx")
plt.scatter('Sales','Quantity',s='City',c=df.Category.astype('category').cat.codes, data=df)


