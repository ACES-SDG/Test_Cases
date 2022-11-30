import tkinter as tk
from tkinter import *
# from  tkinter.dnd import *
from tkinter.dnd import DndHandler
from tkinter.dnd import dnd_start
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
import os
from matplotlib.backend_bases import MouseEvent
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from tkinter import filedialog as fd
import pandas as pd
import openpyxl
import numpy as np


def graphs(root, df):
    colsPanel = Frame(root, width=200, bg='grey', relief=SUNKEN)
    colsPanel.pack_propagate(0)
    colsPanel.pack(side=RIGHT, fill='y')

    columnList = list(df.columns)
    columnList.pop(0)
    columnListVar = tk.StringVar(value=columnList)
    colList = Listbox(colsPanel, width=60,
                      listvariable=columnListVar,
                      height=20, selectmode=SINGLE, borderwidth=None
                      )
    colList.config(bg='grey')
    print(columnList)
    print(len(columnList))
    colList.pack(expand=True, side=TOP)


    
    

    def selectRow():
        global row
        row = colList.get(colList.curselection())
        print(row)

    def selectcolumn():
        global column
        column = colList.get(colList.curselection())
        print(column)

    def canvas_click_event(event):
        print('Clicked canvas: ', event.x, event.y, event.widget)

        pass
    def plot_graph():
        global fig
        x = str(column)
        y = str(row)

        x = int(df[x].sum())
        y = int(df[y].sum())
        fig = plt.figure(figsize=(6, 4))
        plt.cla()
        plt.clf()

        # for i in range(0, len(y)):
        #     y[i] = int(y[i])
        # for i in range(0, len(x)):
        #     x[i] = str(x[i])
        plt.plot(x, y,'o')
        # if selected=='Line Graph':
        #   plt.xticks(rotation='vertical')
        #  plt.plot(x, y)
        # elif selected=='Bar Chart':
        #   plt.bar(x,y)
        # elif selected=='Pie Chart':
        #   plt.pie(x,y)
        # elif selected=='Box Plot':
        #   plt.box(x,y)
        
        canvas = FigureCanvasTkAgg(fig,
                                    master=root, )
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM)
        print(root.winfo_children())
        def on_press(event):
            print('you pressed', event.button, event.x, event.y)

        cid = canvas.mpl_connect('button_press_event', on_press)
        # canvas.bind('<Button-1>',canvas_click_event)

    colBtn = Button(colsPanel, bg='#5792f5', text='Select Column', width=10, height=1, command=selectcolumn)
    colBtn.pack()

    rowBtn = Button(colsPanel, bg='#5792f5', text='Select Row', width=10, height=1, command=selectRow)
    rowBtn.pack()


    plotBtn = Button(colsPanel, bg='#5792f5', text='Plot a Graph', width=11, height=1, command=plot_graph)
    plotBtn.pack()


    sheetpanel = Frame(root, width=200, bg='lightgrey', height=40)
    sheetpanel.pack_propagate(0)
    sheetpanel.pack(side=TOP, fill='x', anchor='ne', padx=70)

    txt = Label(sheetpanel,height=15, width=30,bg='yellow')
    txt.pack(side=TOP)
    txt.pack_propagate(0)

    

    
    
    
    # options = ('Line Graph', 'Bar Chart', 'Pie Chart', 'Box PLot')
    # selected = StringVar()
    # selected.set('Line Graph')
    # selectgraph = OptionMenu(sheetpanel, selected, *options)
    # selectgraph.pack()

    pass
