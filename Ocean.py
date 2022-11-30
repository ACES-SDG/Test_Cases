import tkinter as tk
from tkinter import *
from tkinter import Menu
from tkinter import messagebox
from tkinter import ttk
import os
from tkinter import filedialog
import pandas as pd
import openpyxl

def open_program():
    my_program = filedialog.askopenfilename()
    my_label.config(text=my_program)
    os.system(my_program)


def ask_qus():
    val = messagebox.askquestion("Exit?", "Do you want to exit?")
    if val == 'yes':
        root.destroy()

def File_dialog():
    """This Function will open the file explorer and assign the chosen file path to label_file"""
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("All Files", "*.*")))

    label_file["text"] = filename
    Load_excel_data()
    return None


def Load_excel_data():
    """If the file selected is valid this will load the file into the Treeview"""
    file_path = label_file["text"]
    try:
        excel_filename = r"{}".format(file_path)
        if excel_filename[-4:] == ".csv":
            df = pd.read_csv(excel_filename)
        else:
            df = pd.read_excel(excel_filename)

    except ValueError:
        tk.messagebox.showerror("Information", "The file you have chosen is invalid")
        return None
    except FileNotFoundError:
        tk.messagebox.showerror("Information", f"No such file as {file_path}")
        return None

    clear_data()
    tv1["column"] = list(df.columns)
    tv1["show"] = "headings"
    for column in tv1["columns"]:
        tv1.heading(column, text=column)  # let the column heading = column name

    df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        tv1.insert("", "end",
                   values=row)  # inserts each list into the treeview. For parameters see https://docs.python.org/3/library/tkinter.ttk.html#tkinter.ttk.Treeview.insert
    return None


def clear_data():
    tv1.delete(*tv1.get_children())
    return None


root = tk.Tk()
root.title("Ocean-Book1")

root.geometry("900x700")

my_label = Label(root, text="")
my_label.pack(pady=20)

# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
data_menu = Menu(menubar)
server_menu = Menu(menubar)
window_menu = Menu(menubar)
help_menu = Menu(menubar)
# add a menu item to the menu

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
    command=lambda: File_dialog()
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

f1 = tk.Frame(root, bg="#e6e6e6", borderwidth=2, width=280, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")
f1.pack_propagate(0)

# f2 = tk.Frame(root, bg="#e6e6e6", borderwidth=1, height=290, relief=SUNKEN)
# f2.pack(side=BOTTOM, anchor="sw", fill="x")
# f2.pack_propagate(0)

frame1 = tk.LabelFrame(root, text="Excel Data", height=500, width=500, )
frame1.pack(side=BOTTOM, fill="x", anchor="sw")
frame1.pack_propagate(0)

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=80, width=400, anchor='ne', rely=0.65, relx=0)

# Buttons
button1 = tk.Button(file_frame, text="Browse A File", )
button1.place(rely=0.65, relx=0.50)

button2 = tk.Button(file_frame, text="Load File", command=lambda: Load_excel_data())
button2.place(rely=0.65, relx=0.30)

# The file/file path text
label_file = ttk.Label(file_frame)
label_file.place()

## Treeview Widget
tv1 = ttk.Treeview(frame1)
tv1.place(relheight=1, relwidth=1)  # set the height and width of the widget to 100% of its container (frame1).

treescrolly = tk.Scrollbar(frame1, orient="vertical",
                           command=tv1.yview)  # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal",
                           command=tv1.xview)  # command means update the xaxis view of the widget
tv1.configure(xscrollcommand=treescrollx.set,
              yscrollcommand=treescrolly.set)  # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget




root.mainloop()
