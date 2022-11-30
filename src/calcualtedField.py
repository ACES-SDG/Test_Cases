import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from numpy import *
import pandas as pd
import numpy as np
from tkinter import ttk
import matplotlib.pyplot as plt


def add_func():
    global columns_list,code_line,columnList,code_line2
    global coloumn_selection, operator_,expression_,True_condition,False_condition
    
    if_label = Label(code_line,text="IF", width=4)
    if_label.pack(side=LEFT)

    
    coloumn_selection = ttk.Combobox(code_line)
    coloumn_selection['values']=columnList
    coloumn_selection.set('Select Field')
    coloumn_selection.pack(side=LEFT)

    operator_ = ttk.Combobox(code_line, width=5)
    operator_['values']=['<','<=','==','>','>=']
    operator_.set('Operator')
    operator_.pack(side=LEFT)

    expression_ = Text(code_line,width=15,height=1 )
    expression_.pack(side=LEFT)

    THEN_label = Label(code_line,text="THEN", width=4)
    THEN_label.pack(side=LEFT)

    True_condition = Entry(code_line,)
    True_condition.pack(side=LEFT)
    True_condition.focus()
    True_condition.insert(0, "True statement")

    ELSE_label = Label(code_line2,text="ELSE", width=4)
    ELSE_label.pack(side=LEFT,anchor='w')

    False_condition = Entry(code_line2)
    False_condition.pack(side=LEFT,anchor='w')
    False_condition.focus()
    False_condition.insert(0, "False statement")


def fetch_code():
    global coloumn_selection, operator_,expression_,True_condition,False_condition
    global df,columns_list


    get_operand  = coloumn_selection.get()
    get_operator = operator_.get()
    get_expression = expression_.get('1.0',END)
    get_true = True_condition.get()
    get_false = False_condition.get()
    
    # print(f'operand:{get_operand}\n operator:{get_operator}\n expression:{get_expression}\n True:{get_true}\n False:{get_false}')

    code = f'df["New_field"]= np.where(df["{get_operand}"]{get_operator}{get_expression},df["{get_true}"],{get_false})'
    exec(code)
    # new_list = list(df.columns)
    # columns_list.delete(0, END)
    columns_list.insert(END,'New_field')

    # plt.bar(df['New_field'],df['Sales'],data=df)
    # plt.show()
    # df.to_excel('C:/Users/acesi/OneDrive/Desktop/Excel_files/syntax convention.xlsx')
    print(df['New_field'].dtype)
    print(df.head(20))

    


def create_field():
    global code_line,code_line2
    calc_window = Toplevel(root)

    code_frame = Frame(calc_window,width=500, height=300)
    code_frame.pack(side=TOP)

    code_line = Frame(code_frame,height=20,width=500, bg='yellow')
    code_line.pack(side=TOP)
    
    code_line2 = Frame(code_frame,height=20,width=500, bg='yellow')
    code_line2.pack(side=TOP)

    IF_btn = Button(calc_window, text='If_function',command=add_func)
    IF_btn.pack(side=BOTTOM)

    OK_Btn = Button(calc_window, text="Ok",width=10,command=fetch_code)
    OK_Btn.pack(side=BOTTOM,anchor='w')


def open_File():
    global df
    path = askopenfilename(initialdir="Desktop",
                                          title="Select A File",
                                          filetype=(('text files','*.csv'),("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    df= pd.read_csv(path)
    show_fields(df)
    
def show_fields(df):
    global columns_list,columnList

    columnList = list(df.columns)
    columnList.pop(0)
    columnListVar = tk.StringVar(value=columnList)

    columns_list = Listbox(root, width=60,
                      listvariable=columnListVar,
                      height=20, selectmode=SINGLE, borderwidth=None)

    columns_list.pack(expand=True, side=TOP)

    
root = Tk()
root.title('Syntax conventions')

file_btn = Button(root, text='import data', command=open_File)
file_btn.pack(side=TOP)


Calc_Btn = Button(root, text='create new field',command=create_field)
Calc_Btn.pack(side=TOP)




root.mainloop()