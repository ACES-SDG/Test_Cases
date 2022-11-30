import os.path
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class Datasource(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title('Sheets')
    self.geometry('1000x750')
    # button
    self.button = ttk.Button(self, text='Connect')
    self.button['command'] = self.button_clicked
    self.button.pack()

  def button_clicked(self):


    global df, df_list, x_axis, y_axis, canvasFlag
    global label_flag,Filepath,DatasourceName
    global prev_count, sheets,Data_source_name
    global column_name, sheet_list
    # if label_flag == True:
    #     for i in range(prev_count):
    #         column_name.destroy()
    #     label_flag = False
    # DataSource.pack(side=TOP,anchor="w")
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
    self.Listbox = tk.Listbox(self,height=5, width=50)
    self.Listbox.pack()
    self.Listbox.insert(END,Data_source_name)
    self.Listbox.bind('<Button-1>',self.sheets_display)

  def sheets_display(self,*arg):
    # sheets.delete(0,END)
    self.sheets = tk.Listbox(self,height=5, width=50)
    self.sheets.pack()
    global Filepath, sheet_list
    df1 = pd.ExcelFile(Filepath)
    sheet_names = df1.sheet_names
    sheet_list = list(sheet_names)
    for sheetlist in sheet_names:
        dfsheet = pd.read_excel(Filepath, sheet_name=sheetlist)
        print(dfsheet.columns)
    for items in sheet_names:
            self.sheets.insert(END, items)
    self.sheets.bind("<<ListboxSelect>>", self.callback)

  # def callback(self,*arg):
  #   global default_sheet,data
  #   selection = event.widget.curselection()
  #   if selection:
  #       index = selection[0]
  #       data = event.widget.get(index)
  #       print(data)
  #       return data
if __name__ == "__main__":
  app = Datasource()
  app.mainloop()