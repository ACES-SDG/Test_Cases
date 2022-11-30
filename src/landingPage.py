from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)



root = Tk()

root.title('Project Ocean - Desktop Version 0.1')
root.geometry('1200x600')

menu_bar = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
menu_bar.pack(side=TOP, fill=X)

# creating a Menubar
menubar = Menu(root)

# Adding File Menu and commands
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='New File', command=None)
file.add_command(label='Open...', command=None)
file.add_command(label='Save', command=None)
file.add_separator()
file.add_command(label='Exit', command=root.destroy)

# Adding Data Menu and commands
Data = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Data', menu=Data)
Data.add_command(label='Cut', command=None)
Data.add_command(label='Copy', command=None)
Data.add_command(label='Paste', command=None)
Data.add_command(label='Select All', command=None)
Data.add_separator()
Data.add_command(label='Find...', command=None)
Data.add_command(label='Find again', command=None)

# Adding Worksheet Menu and commands
Worksheet = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Worksheet', menu=Worksheet)
Worksheet.add_command(label='Cut', command=None)
Worksheet.add_command(label='Copy', command=None)
Worksheet.add_command(label='Paste', command=None)
Worksheet.add_command(label='Select All', command=None)
Worksheet.add_separator()
Worksheet.add_command(label='Find...', command=None)
Worksheet.add_command(label='Find again', command=None)

# Adding Dashboard Menu and commands
Dashboard = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Dashboard', menu=Dashboard)
Dashboard.add_command(label='Cut', command=None)
Dashboard.add_command(label='Copy', command=None)
Dashboard.add_command(label='Paste', command=None)
Dashboard.add_command(label='Select All', command=None)
Dashboard.add_separator()
Dashboard.add_command(label='Find...', command=None)
Dashboard.add_command(label='Find again', command=None)

# Adding Story Menu and commands
Story = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Story', menu=Story)
Story.add_command(label='Cut', command=None)
Story.add_command(label='Copy', command=None)
Story.add_command(label='Paste', command=None)
Story.add_command(label='Select All', command=None)
Story.add_separator()
Story.add_command(label='Find...', command=None)
Story.add_command(label='Find again', command=None)

# Adding Analysis Menu and commands
Analysis = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Analysis', menu=Analysis)
Analysis.add_command(label='Cut', command=None)
Analysis.add_command(label='Copy', command=None)
Analysis.add_command(label='Paste', command=None)
Analysis.add_command(label='Select All', command=None)
Analysis.add_separator()
Analysis.add_command(label='Find...', command=None)
Analysis.add_command(label='Find again', command=None)

# Adding Map Menu and commands
Map = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Map', menu=Map)
Map.add_command(label='Cut', command=None)
Map.add_command(label='Copy', command=None)
Map.add_command(label='Paste', command=None)
Map.add_command(label='Select All', command=None)
Map.add_separator()
Map.add_command(label='Find...', command=None)
Map.add_command(label='Find again', command=None)

# Adding Format Menu and commands
Format = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Format', menu=Format)
Format.add_command(label='Cut', command=None)
Format.add_command(label='Copy', command=None)
Format.add_command(label='Paste', command=None)
Format.add_command(label='Select All', command=None)
Format.add_separator()
Format.add_command(label='Find...', command=None)
Format.add_command(label='Find again', command=None)

# Adding Server Menu and commands
Server = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Server', menu=Server)
Server.add_command(label='Cut', command=None)
Server.add_command(label='Copy', command=None)
Server.add_command(label='Paste', command=None)
Server.add_command(label='Select All', command=None)
Server.add_separator()
Server.add_command(label='Find...', command=None)
Server.add_command(label='Find again', command=None)

# Adding Window Menu and commands
Window = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Window', menu=Window)
Window.add_command(label='Cut', command=None)
Window.add_command(label='Copy', command=None)
Window.add_command(label='Paste', command=None)
Window.add_command(label='Select All', command=None)
Window.add_separator()
Window.add_command(label='Find...', command=None)
Window.add_command(label='Find again', command=None)

# Adding Help Menu
help_ = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help_)
help_.add_command(label='Tk Help', command=None)
help_.add_command(label='Demo', command=None)
help_.add_separator()
help_.add_command(label='About Tk', command=None)

# Menu Icons

menu_icon_bar = Frame(root, borderwidth=6, bg="white", relief=GROOVE)
menu_icon_bar.pack(side=TOP, anchor="nw", fill=X)

icon1 = PhotoImage(file="icon1.png")
icon2 = PhotoImage(file="icon2.png")
icon3 = PhotoImage(file="icon3.png")
icon4 = PhotoImage(file="icon4.png")
icon5 = PhotoImage(file="icon5.png")
icon6 = PhotoImage(file="icon6.png")
icon7 = PhotoImage(file="icon7.png")
icon8 = PhotoImage(file="icon8.png")
icon9 = PhotoImage(file="icon9.png")
icon10 = PhotoImage(file="icon10.png")
icon11 = PhotoImage(file="icon11.png")
icon12 = PhotoImage(file="icon12.png")
icon13 = PhotoImage(file="icon13.png")
icon14 = PhotoImage(file="icon14.png")
icon15 = PhotoImage(file="icon15.png")
icon16 = PhotoImage(file="icon16.png")
icon17 = PhotoImage(file="icon17.png")
icon18 = PhotoImage(file="icon18.png")
icon19 = PhotoImage(file="icon19.png")
icon20 = PhotoImage(file="icon20.png")
icon21 = PhotoImage(file="icon21.png")




b1 = Button(menu_icon_bar, image=icon1, width=30, height=30)
b1.pack(side=LEFT, padx=7, pady=3)

b2 = Button(menu_icon_bar, image=icon2, width=30, height=30)
b2.pack(side=LEFT, padx=7, pady=3)

b3 = Button(menu_icon_bar, image=icon3, width=30, height=30)
b3.pack(side=LEFT, padx=7, pady=3)

b4 = Button(menu_icon_bar, image=icon4, width=30, height=30)
b4.pack(side=LEFT, padx=7, pady=3)

b5 = Button(menu_icon_bar, image=icon5, width=30, height=30)
b5.pack(side=LEFT, padx=7, pady=3)

b6 = Button(menu_icon_bar, image=icon6, width=30, height=30)
b6.pack(side=LEFT, padx=7, pady=3)

b7 = Button(menu_icon_bar, image=icon7, width=30, height=30)
b7.pack(side=LEFT, padx=7, pady=3)

b8 = Button(menu_icon_bar, image=icon8, width=30, height=30)
b8.pack(side=LEFT, padx=7, pady=3)

b9 = Button(menu_icon_bar, image=icon9, width=30, height=30)
b9.pack(side=LEFT, padx=7, pady=3)

b10 = Button(menu_icon_bar, image=icon10, width=30, height=30)
b10.pack(side=LEFT, padx=7, pady=3)

b11 = Button(menu_icon_bar, image=icon11, width=30, height=30)
b11.pack(side=LEFT, padx=7, pady=3)

b12 = Button(menu_icon_bar, image=icon12, width=30, height=30)
b12.pack(side=LEFT, padx=7, pady=3)

b13 = Button(menu_icon_bar, image=icon13, width=30, height=30)
b13.pack(side=LEFT, padx=7, pady=3)

b14 = Button(menu_icon_bar, image=icon14, width=30, height=30)
b14.pack(side=LEFT, padx=7, pady=3)

b15 = Button(menu_icon_bar, image=icon15, width=30, height=30)
b15.pack(side=LEFT, padx=7, pady=3)

b16 = Button(menu_icon_bar, image=icon16, width=30, height=30)
b16.pack(side=LEFT, padx=7, pady=3)

b17 = Button(menu_icon_bar, image=icon17, width=30, height=30)
b17.pack(side=LEFT, padx=7, pady=3)

b18 = Button(menu_icon_bar, image=icon18, width=30, height=30, command="")
b18.pack(side=LEFT, padx=7, pady=3)


def show():
    label.config(text=clicked.get())

# Dropdown menu options
options = [
    "Standard",
    "Fit Width",
    "Fit Height",
    "Entire View"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Standard")

# Create Dropdown menu
drop = OptionMenu(menu_icon_bar, clicked, *options)
drop.pack(side=LEFT, padx=7, pady=3)

# # Create button, it will change label text
# button = Button(root, text="click Me", command=show).pack()

b19 = Button(menu_icon_bar, image=icon19, width=30, height=30)
b19.pack(side=LEFT, padx=7, pady=3)

b20 = Button(menu_icon_bar, image=icon20, width=30, height=30)
b20.pack(side=LEFT, padx=7, pady=3)

b21 = Button(menu_icon_bar, image=icon21, width=30, height=30)
b21.pack(side=LEFT, padx=7, pady=3)





import_data = Frame(root, borderwidth=6, bg="#D3D3D3", width=300, relief=GROOVE)
import_data.pack(side=LEFT, anchor="nw", fill=Y)
# import_data.pack_propagate(0)

# labelTest = Label(import_data, text="Hello world",width =35)
# labelTest.pack()

import_buttons = Frame(import_data)
import_buttons.pack(side=TOP, anchor="nw", fill=X)


data_but = Button(import_buttons, text="Data", width=20)
data_but.pack(side=LEFT, anchor="nw", fill=X)

analytics_but = Button(import_buttons, text="Analytics", width=20)
analytics_but.pack(side=LEFT, anchor="nw", fill=X)

label_flag = False
prev_count = 0

file_path = Label(import_data, bg="#D3D3D3")
file_path.pack(side= TOP , fill=X)



# lbx = Listbox(import_data, bg="#D3D3D3",  fg="#800000", height=prev_count-1, bd=0, selectmode=MULTIPLE)






global x_axis, y_axis, canvasFlag

canvasFlag = 0
def plot():



    global x,y, x_col, y_col, df, flag, canvasFlag

    # for i in lbx.curselection():
    #     choice_list.append(lbx.get(i))

    if plotting_frame.winfo_ismapped():
        pass
    else:
        plotting_frame.pack(side=TOP, anchor="n")

    x_axis_option = x_axis.get()
    y_axis_option = y_axis.get()
    x = str(x_axis_option)
    y = str(y_axis_option)
    print(x, y)

    XLabel = Label(import_data, text="X Axis : " + x, bg="#D3D3D3")
    XLabel.pack(fill=X)
    YLabel = Label(import_data, text="Y Axis : " + y, bg="#D3D3D3")
    YLabel.pack(fill=X)

    x_col = df.columns.get_loc(x)
    y_col =  df.columns.get_loc(y)

    # x_col = list(df[x])
    # y_col = list(df[y])

    print(x_col, y_col)
    # the figure that will contain the plot
    fig = Figure(figsize=(10, 7),
                 dpi=100)


    # adding the subplot
    plot1 = fig.add_subplot(111)

    x_col = df[x].to_numpy()
    y_col = df[y].to_numpy()



    # creating the Tkinter canvas
    # containing the Matplotlib figure

    # if (canvasFlag == 1):
    #     canvas.delete('all')





    canvasFlag = 1

    canvas = FigureCanvasTkAgg(fig,master=plotting_frame)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()





    plot__menu = plot_menu.get()
    if plot__menu == "Bar Graph":
        plot1.bar(x_col,y_col)
    elif plot__menu == "Line Graph":
        plot1.plot(x_col, y_col)
    elif plot__menu == "Scatter Plot":
        plot1.scatter(x_col, y_col)
    # elif plot__menu == "Pie Graph":
    #     plot1.pie(x_col, radius=1, labels=stockListExp,autopct='%0.2f%%', shadow=True)
    elif plot__menu == "Step Graph":
        plot1.step(x_col, y_col)
    elif plot__menu == "Stem Graph":
        plot1.stem(x_col, y_col)
    else:
        plot1.bar(x_col, y_col)
    # plot1.bar(x_col, y_col)




    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


    if plotting_frame.winfo_ismapped():
        def canvasClear():
            # for item in canvas.get_tk_widget().find_all():
            #     canvas.get_tk_widget().delete(item)
            plotting_frame.pack_forget()
            XLabel.config(text="")
            YLabel.config(text="")
    clearCanvas = Button(import_data, text="clear", command=canvasClear)
    clearCanvas.pack()




global df_list
df_list = []

def openFile():
    global df, df_list, x_axis, y_axis, canvasFlag
    global label_flag
    global prev_count
    global column_name
    if label_flag == True:
        for i in range(prev_count):
            column_name.destroy()
        label_flag = False







    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    file_path["text"] = filepath
    file.close()
    df = pd.read_excel(filepath)
    print(df.columns)
    df_list = list(df)
    prev_count = len(df_list)

    df = pd.DataFrame(df)

    # X Axis selection
    x_axis_frame = Frame(import_data, bg="#D3D3D3")
    x_axis_frame.pack(side=TOP, anchor="n")

    x_axis_label = Label(x_axis_frame, text="X-axis : ", bg="#D3D3D3")
    x_axis_label.pack(side=LEFT, pady = 20, padx=10)

    x_axis = StringVar()
    x_axis.set("Select")

    x_axis_dropdown = OptionMenu(x_axis_frame, x_axis, *df_list)
    # x_axis_dropdown.config(bg="#D3D3D3")
    x_axis_dropdown.pack(side=LEFT)

    # Y Axis selection
    y_axis_frame = Frame(import_data, bg="#D3D3D3")
    y_axis_frame.pack(side=TOP, anchor="n")

    y_axis_label = Label(y_axis_frame, text="Y-axis : ", bg="#D3D3D3")
    y_axis_label.pack(side=LEFT, pady = 20, padx=10)

    y_axis = StringVar()
    y_axis.set("Select")

    y_axis_dropdown = OptionMenu(y_axis_frame, y_axis, *df_list)
    # y_axis_dropdown.config(bg="#D3D3D3")
    y_axis_dropdown.pack(side=LEFT)

    plot_button = Button(import_data, command=plot, text="Plot")
    plot_button.pack()

    # column_name = Label(import_data , bg="#D3D3D3" , fg="#800000")
    # column_name.pack(side=TOP, anchor="n")

    # for i in range(len(df_list) - 1):
    #     column_name["text"] += "\n" + df_list[i] + "\n"



    # for i in range(len(df_list) - 1):
    #     lbx.insert(i, df_list[i] )
    #     lbx.pack()




# def clearData():
        # lbx.delete(0, last=prev_count-1)
        # file_path["text"] = ""
        # #file_path.destroy()






data_but = Button(import_data, text="Connect to Data", command=openFile)
data_but.pack(side=TOP, anchor="center", fill=X, pady=15)



# clear_col = Button(import_data, text="Clear Data", command="")
# clear_col.pack(side=TOP, anchor="center", fill=X)


plot_menu = StringVar()
plot_menu.set("Select the plot")

plot_drop= OptionMenu(import_data, plot_menu,"Bar Graph", "Line Graph","Scatter Plot", "Pie Graph", "Step Graph", "Stem Graph")
plot_drop.pack(side = TOP, anchor="n")


# PLOTTING GRAPHS

x = 0
y= 0
choice_list = []


plotting_frame = Frame(root)
plotting_frame.pack(side=TOP, anchor="n")

x_col = 0
y_col = 0
flag = 0









root.config(menu=menubar)

root.mainloop()
