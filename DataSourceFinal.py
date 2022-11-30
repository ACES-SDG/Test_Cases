import os.path
import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import numpy as np


# from Button import sheetsFunc
def Datapivot():
    global join
    selected = treev.focus()
    print(selected)
    temp = treev.item(selected, 'values')
    print(temp)
    table = pd.pivot_table(join, index=temp)
    print(table)


global sheet_list, sheets
global default_sheet, data, DatasourceName


# def right(event):
#      click=event.widget.curselection()
#      try:
#           root2x = event.widget.wininfo_root2x()
#           root2y = event.widget.wininfo_root2y()
#           itemx,itemy,itemwidth,itemheight = event.widget.bbox(click)
#           select_u_j.tk_popup(root2x+event.widget.wininfo_width-10, root2y+itemy+10)
#      finally:
#           select_u_j.grab_release()
# if click:
#     print("working")
# data_comb.pack()
#
#     combination_type = select_u_j.get()
#     if combination_type:
#         data_comb.pack_forget()
#         if combination_type=="Union":
#             print("Union")
#         else:
#             print("Join")
def SelectsheetFunction():
    global default_sheet, data, deafaultsheet, secondsheet
    global join, var, option
    option = [default_sheet, data, 'Output Sheet']
    dropdown_j_u = OptionMenu(sideframe3, Select_sheet, *option)
    dropdown_j_u.pack(side=BOTTOM)

    OptionsButton.pack(side=BOTTOM)
    dropdown_j_u.pack(side=BOTTOM)


def options():
    global default_sheet, data, deafaultsheet, secondsheet
    global join, var, option

    sheet_request = Select_sheet.get()
    # else:
    # if sheet_request:
    print(sheet_request)
    clear_data()
    if sheet_request == default_sheet:
        # print("okk")
        defaultsheet = pd.read_excel(Filepath, sheet_name=default_sheet)
        secondsheet = pd.read_excel(Filepath, sheet_name=data)
        treev["column"] = list(defaultsheet.columns)
        treev["show"] = "headings"
        for cols in treev["columns"]:
            treev.heading(cols, text=cols)  # let the column heading = column name

        df_rows = join.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            treev.insert("", "end",
                         values=row)
    elif sheet_request == data:
        defaultsheet = pd.read_excel(Filepath, sheet_name=default_sheet)
        secondsheet = pd.read_excel(Filepath, sheet_name=data)
        treev["column"] = list(secondsheet.columns)
        treev["show"] = "headings"
        for cols in treev["columns"]:
            treev.heading(cols, text=cols)  # let the column heading = column name

        df_rows = join.to_numpy().tolist()  # turns the dataframe into a list of lists
        for row in df_rows:
            treev.insert("", "end",
                         values=row)
    else:
        defaultsheet = pd.read_excel(Filepath, sheet_name=default_sheet)
        secondsheet = pd.read_excel(Filepath, sheet_name=data)
        join_union()


def merge_():
    global default_sheet, data, deafaultsheet, secondsheet
    global join, var
    clear_data()
    defaultsheet = pd.read_excel(Filepath, sheet_name=default_sheet)
    secondsheet = pd.read_excel(Filepath, sheet_name=data)
    var = " "
    for i in defaultsheet.columns:
        if i in secondsheet:
            print(i)
            join = defaultsheet.merge(secondsheet, on=i, how="left")
            join_union()
            var = "OK"
        # else:
    #     #   print("Error")
    # for i in defaultsheet.columns
    if var == ' ':
        tk.messagebox.showerror("ERROR", "No Common Columns Between \n The Selected Sheets")
    #         print("error")
    # # join.to_excel("result.xlxs", index = False)
    #  join.to_csv('stilltesting.csv')
    # print(join.to_string())
    # join_union()

    #     print("error")
    # option = [default_sheet, data, 'Output Sheet']
    # dropdown_j_u = OptionMenu(sideframe3, Select_sheet, *option)

    # OptionsButton.pack(side=BOTTOM)
    # dropdown_j_u.pack(side=BOTTOM)
    SelectsheetFunction()


def union():
    global default_sheet, data, deafaultsheet, secondsheet, join, k
    clear_data()
    # OptionsButton.pack(side=BOTTOM)
    # dropdown_j_u.pack(side=BOTTOM)
    var = " "
    defaultsheet = pd.read_excel(Filepath, sheet_name=default_sheet)
    secondsheet = pd.read_excel(Filepath, sheet_name=data)
    for i in defaultsheet.columns:
        if i in secondsheet:
            global join
            print(i)
            frames = [defaultsheet, secondsheet]
            join = pd.concat(frames)
            join_union()
            var = "OK"

    if var == ' ':
        tk.messagebox.showerror("ERROR", "No Common Rows Between \n The Selected Sheets")
        # join=defaultsheet.merge(secondsheet,on=i,how="left")
    # join.to_excel("result.xlxs", index = False)
    #  join.to_csv('stilltesting.csv')
    # print(join.to_string())

    #     print("error")
    SelectsheetFunction()


def join_union():
    clear_data()
    # if k==1:
    #  root2.messagebox.showerror("showerror", "Error")

    treev["column"] = list(join.columns)
    treev["show"] = "headings"
    for cols in treev["columns"]:
        treev.heading(cols, text=cols)  # let the column heading = column name

    df_rows = join.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        treev.insert("", "end",
                     values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert


def clear_data():
    treev.delete(*treev.get_children())
    return None


def go(event):
    global default_sheet
    cs = sheets.curselection()
    if cs:
        index1 = cs[0]
        default_sheet = event.widget.get(index1)
        display.config(text=default_sheet)
        print(default_sheet)
        return default_sheet


def callback(event):
    global default_sheet, data
    selection = event.widget.curselection()
    if selection:
        print('my slection - selection[0]',selection[0])
        index = selection[0]
        data = event.widget.get(index)
        print(data)
        return data


def openFile():
    global df, df_list, x_axis, y_axis, canvasFlag
    global label_flag, Filepath, DatasourceName
    global prev_count, sheets, Data_source_name
    global column_name, sheet_list
    # if label_flag == True:
    #     for i in range(prev_count):
    #         column_name.destroy()
    #     label_flag = False

    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    # file_path["text"] = filepath
    Filepath = filepath
    file.close()
    pathname, extension = os.path.splitext(Filepath)
    DatasourceName = pathname.split('/')
    Data_source_name = DatasourceName[-1]
    print(Data_source_name)
    # df = pd.read_excel(filepath)
    # print(df.columns)
    # df_list = list(df)
    # prev_count = len(df_list)
    # df1 = pd.ExcelFile(filepath)

    df1 = pd.ExcelFile(filepath)
    sheet_names = df1.sheet_names

    for sheetlist in sheet_names:
        dfsheet = pd.read_excel(filepath, sheet_name=sheetlist)
        print(dfsheet.columns)
    DataSource.pack(side=TOP)
    sheets.pack()
    Datalbl = Label(DataSource, text=Data_source_name, height=1, width=25)
    Datalbl.pack()
    data_but.pack(side=LEFT, anchor="center", fill=X)
    data_but1.pack(side=LEFT, anchor="center", fill=X)
    # new_var=sheets.get(ANCHOR)
    # print(new_var)
    for items in sheet_names:
        sheets.insert(END, items)

    # dfs = pd.read_excel(filepath,sheet_name='People')

    sheet_list = list(sheet_names)
    # print(sheet_list)
    # f3 = dfsheet.merge(dfsheet, on="Order ID", how="left")
    # # print(f3.columns)
    # f3.to_excel("Results.xlsx", index=False)


def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    os.system(my_program)


def ask_qus():
    val = messagebox.askquestion("Exit?", "Do you want to exit?")
    if val == 'yes':
        root2.destroy()
    return None


# for items in sheet_list:
#    # #     df2 = pd.read_excel(items)white
#    #     print(df2)
#      sheets = Listbox(sideframe2)
#      sheets.insert(END, items)
#    sheetsFunc(sheet_list)
root2 = Tk()
root2.title('Tableau v0.0.1')
root2.geometry('1200x600')
root2.configure(bg='white')
global DatasourceName, Data_source_name
global default_sheet, data, DatasourceName
my_label = Label(root2, text="")
my_label.pack(pady=20)
menubar = Menu(root2)
root2.config(menu=menubar)
# create a menu
file_menu = Menu(menubar)
data_menu = Menu(menubar)
server_menu = Menu(menubar)
window_menu = Menu(menubar)
help_menu = Menu(menubar)
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# add the File menu to the menubar

file_menu.add_command(
    label='New',
    command=''
)
file_menu.add_command(
    label='Open',
    command=open_program
)
file_menu.add_separator()
file_menu.add_command(
    label='Paste',
    command=''
)
file_menu.add_command(
    label='Exit',
    command=ask_qus
)
menubar.add_cascade(
    label="Data",
    menu=data_menu
)
data_menu.add_command(
    label='New Data Source',
    command=lambda: openFile()
)
data_menu.add_separator()
data_menu.add_command(
    label='Refresh Data Source',
    command=''
)
data_menu.add_command(
    label='Duplicate Data Source',
    command=''
)
data_menu.add_command(
    label='Close Data Source',
    command=''
)
menubar.add_cascade(
    label="Server",
    menu=server_menu
)
menubar.add_cascade(
    label="Window",
    menu=window_menu
)
menubar.add_cascade(
    label="Help",
    menu=help_menu
)

sideframe = Frame(root2, borderwidth=16, relief=FLAT, bg='yellow', width=300, height=250)
sideframe.pack(side=LEFT, anchor=NW, fill=Y)

DataSource = LabelFrame(sideframe, height=5, width=50)
sideframe.pack_propagate(0)

bottomline = Frame(root2, height=2, width=500, bg='white')
bottomline.pack(side=BOTTOM, fill='x')
# sideframe2 = Frame(root2, borderwidth=6, relief=FLAT, width=300, height=50)
# sideframe2.pack(side=LEFT, anchor=NW, fill=Y)
# # sheets.insert(END)


sheets = Listbox(sideframe, height=5, width=50)
sheets.bind("<<ListboxSelect>>", callback)

sheets.bind('<Button-3>', go)
# sheets.bind_class('<<Button-3>>', right)

select_u_j = Menu(sheets)
select_u_j.add_command(label="join")
select_u_j.add_separator()
select_u_j.add_command(label="union")
# datatype of menu text
Select_sheet = StringVar()
# initial menu text
# Select_sheet.set("")

tabledisplay = LabelFrame(root2, text="Data Set", height=500, width=500, )
tabledisplay.pack(side=BOTTOM, fill="x", anchor="sw")
tabledisplay.pack_propagate(0)
# pivot_btn = Button(sideframe, command=Datapivot).pack()
# DataSource = Label(sideframe,text=DatasourceName)
# DataSource.pack()
# print(sheet_request)

# =====================================TREE VIEW FOR TABULAR DISPLAY =========================================

treev = ttk.Treeview(tabledisplay)
treev.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).
treescrollery = Scrollbar(tabledisplay, orient="vertical",
                          command=treev.yview)  # command means update the yaxis view of the widget
treescrollerx = Scrollbar(tabledisplay, orient="horizontal",
                          command=treev.xview)  # command means update the xaxis view of the widget
treev.configure(xscrollcommand=treescrollerx.set,
                yscrollcommand=treescrollery.set)  # assign the scrollbars to the Treeview Widget
treescrollerx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
treescrollery.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

label_file = ttk.Label(bottomline)
label_file.pack(side=LEFT)

sideframe3 = Frame(root2, borderwidth=16, bg='white', relief=FLAT, width=900, height=50)
sideframe3.pack(side=LEFT, anchor=NW, fill=Y)
display = Label(sideframe3, text="", bg='white', height=5, width=50)
display.pack()

# treev.bind('<Button-1>',Datapivot)

cdata_but = Button(sideframe, text="Connect to Data", command=openFile)
cdata_but.pack(side=BOTTOM, anchor="s", fill=X)
data_but = Button(sideframe, text="join", height=1, width=25, command=merge_)
data_but1 = Button(sideframe, text="union", height=1, width=25, command=union)
OptionsButton = Button(sideframe3, text="Select", height=1, width=25, command=options)
# dropdown_j_u.bind('<Button-1>',options)
root2.mainloop()
