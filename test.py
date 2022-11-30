import os.path
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
def sheet_display(event):
    sheets.configure()
    global Filepath, sheet_list
    df1 = pd.ExcelFile(Filepath)
    print(Filepath,'filepath')
    sheet_names = df1.sheet_names
    print(sheet_names,'sheet_names')
    sheet_list = list(sheet_names)
    print(sheet_list,"sheet_list")
    for sheetlist in sheet_names:
        dfsheet = pd.read_excel(Filepath, sheet_name=sheetlist)
        print(dfsheet.columns)
    for items in sheet_names:
            sheets.insert(END, items)

def openFile():
    global df, df_list, x_axis, y_axis, canvasFlag
    global label_flag,Filepath,DatasourceName
    global prev_count, sheets,Data_source_name
    global column_name, sheet_list
    # if label_flag == True:
    #     for i in range(prev_count):
    #         column_name.destroy()
    #     label_flag = False
    DataSource.pack(side=TOP,anchor="w")
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    # file_path["text"] = filepath
    Filepath=filepath
    file.close()
    pathname, extension = os.path.splitext(Filepath)
    DatasourceName = pathname.split('/')
    Data_source_name=DatasourceName[-1]
    print(Data_source_name)
    # df = pd.read_excel(filepath)
    # print(df.columns)
    # df_list = list(df)
    # prev_count = len(df_list)
    # df1 = pd.ExcelFile(filepath)


    # Datalbl = Label(DataSource, text=Data_source_name, height=1, width=25)
    # Datalbl.pack(side=TOP,anchor="w")
    sheets.pack()
    Datalbl.pack()

    # new_var=sheets.get(ANCHOR)
    # print(new_var)

    # for items in Data_source_name:
    Datalbl.insert(END,Data_source_name)
    # dfs = pd.read_excel(filepath,sheet_name='People')
    Datalbl.bind('<Button-1>',sheet_display)

    # print(sheet_list)
    # f3 = dfsheet.merge(dfsheet, on="Order ID", how="left")
    # # print(f3.columns)
    # f3.to_excel("Results.xlsx", index=False)


# for items in sheet_list:
#    # #     df2 = pd.read_excel(items)
#    #     print(df2)
#      sheets = Listbox(sideframe2)
#      sheets.insert(END, items)
#    sheetsFunc(sheet_list)
root = Tk()
root.title('Tableau v0.0.1')
root.geometry('1200x600')
root.configure(bg='grey')
sideframe = Frame(root, borderwidth=16, relief=SUNKEN, width=30, height=250)
sideframe.pack(side=LEFT, anchor=NW, fill=Y)


bottomline = Frame(root, height=2, width=500,bg='#fff')
bottomline.pack(side=BOTTOM, fill='x')
sideframe2 = Frame(root, borderwidth=6, relief=SUNKEN, width=300, height=50)
sideframe2.pack(side=LEFT, anchor="nw", fill=Y)
sheets = Listbox(sideframe, height=5, width=50)
Datalbl= Listbox(sideframe, height=5, width=50)
data_but = Button(sideframe, text="Connect to Data", command=openFile)
data_but.pack(side=BOTTOM, anchor="center", fill=X)
DataSource = LabelFrame(sideframe,height=5, width=20)
sheets.pack(side=LEFT)
root.mainloop()
