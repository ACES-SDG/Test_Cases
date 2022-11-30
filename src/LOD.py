import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
app = tk.Tk()

# lable = tk.Label(app, text='is it ok',font=30,height=5).pack(side='top',fill='x')
app.geometry('1100x700')

df = pd.read_excel("C:/Users/Mazhar/OneDrive/Desktop/LIve_Working/Ocean Pro V_3.0.0/Excel_files/sales.xlsx")

# fig , ax = plt.subplots(1,2)

fig, ax = plt.subplots(figsize=(7, 5), sharex=True)


# dfd = df.groupby(['Category','Region']).aggregate({'Sales':sum}).unstack(-2)

# fig= dfd.plot( kind='bar' ,subplots=True)

df_central = df[df['Region']=='Central']
df_west = df[df['Region']=='West']
df_South = df[df['Region']=='South']
df_East = df[df['Region']=='East']

plt.subplot(4,4,1)
plt.bar(df_central['Category'],df_central['Sales'])
plt.axis('off')
plt.subplot(4,4,2)
plt.bar(df_East['Category'],df_East['Sales'])
plt.axis('off')
plt.subplot(4,4,3)
plt.bar(df_South['Category'],df_South['Sales'])
plt.axis('off')

plt.subplot(4,4,4)
plt.bar(df_west['Category'],df_west['Sales'])
plt.axis('off')


plt.subplot(4,4,5)
plt.bar(df_central['Category'],df_central['Quantity'])
# plt.axis('off')
plt.xticks(rotation=90)

plt.subplot(4,4,6)
plt.bar(df_East['Category'],df_East['Quantity'])
plt.xticks(rotation=90)

# plt.axis('off')
plt.subplot(4,4,7)
plt.bar(df_South['Category'],df_South['Quantity'])
# plt.axis('off')
plt.xticks(rotation=90)

plt.subplot(4,4,8)
plt.bar(df_west['Category'],df_west['Quantity'])
# plt.axis('off')
plt.xticks(rotation=90)




# plt.hlines['top'].set_visible(False)


# fig.add_subplot()

my_frame = tk.Frame(app)
my_frame.pack(fill='x')

canvas = FigureCanvasTkAgg(fig, master= my_frame)
canvas.draw()

canvas.get_tk_widget().pack()



# plt.show()
app.mainloop()