import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def open_file():
    global df
    path = askopenfilename(initialdir="Desktop",
                                          title="Select A File",
                                          filetypes=(("xlsx files", "*.xlsx"),('text files','*.csv')))
    df= pd.read_excel(path)
    print(df.columns)

def plot_graph():
    print(df.shape)
    # fig , ax = plt.subplots()
    process()
    fig  = sales_plot_axis.get_figure()
    plt.rcParams["figure.autolayout"] = True
    canvas_plot = FigureCanvasTkAgg(fig, my_graph_pane)
    canvas_plot.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
    plt.xticks(rotation=360)
    # ax.plot('Category','Sales',data=df)
    # 

    # ax.add_child_axes(sales_plot)
    # ax.set_axis_off()
    # ax.autoscale_view()
def process():
    global sales_plot_axis
    df_any_one_year = df[df['Order Date'].dt.year == 2018]
    sales_of_2018_with_quarters = df_any_one_year.groupby([df_any_one_year['Order Date'].dt.quarter, 'Category']).aggregate({'Sales':sum})
    sales_plot_axis = sales_of_2018_with_quarters.unstack(-2).plot(kind='bar',figsize=(10,6),title='Sales of all Quarter in 2018')
    # plt.show()
    plt.rcParams["figure.autolayout"] = True
    print('year selected is ',df_any_one_year['Order Date'].dt.year.unique())
root = tk.Tk()
 
file_button = ttk.Button(root,command=open_file,text='open file')
file_button.pack()

plot_button = ttk.Button(root,command=plot_graph,text='plot graph')
plot_button.pack()

my_graph_pane = ttk.Frame()
my_graph_pane.pack()


root.mainloop()