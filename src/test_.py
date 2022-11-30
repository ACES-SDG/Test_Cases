from calendar import c
from matplotlib.figure import Figure
import pandas as pd
from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)

# import seaborn as sns
import numpy as np
from setuptools import Command


global dataframes,fields,df
def Filter_pop():
    pass


filer = 0
def Filter():

    selected_name = str((fields.get(ACTIVE)))

    s = df[selected_name].unique()
    filter_data =Frame(f3, width =180 , height=5)
   # Checkbutton = Listbox
    filter_data.pack()
    filter_data.destroy()
    # for i in s:
    #   filter_data.pack(END,i)
    var = IntVar()
 
    for chbox in s:
        c = Checkbutton(f3,text=chbox, command=filter_data.destroy)
        c.pack()

    exclude_btn = Button(f3,text='Exclude',command=delete_from_graph).pack()

# Checkbutton.config(test='task')

def delete_from_graph():
    print('Excluded',df[df['Category']=="Furniture"].index)
    
  
    ind =list(df[df["Category"]=="Furniture"].index)
    print(ind,'     line no         51')
    
    i=f
    f = df.drop(df.index[ind],axis=0)
    # f = df.drop( index='Category',level=1)
    # f = df.drop(index = ('Category','Furniture'))

    # f = df.drop(index='Profit')
    print(f.shape)
    print(df.shape)

def upload_btn():
      
    global fields,dataframes,df
    
    filename = filedialog.askopenfilename( filetypes=[('All files','.*'),('Excel file','.xlsx'),('Text file','.csv')])
    # print(filename[-4],'===========================================================')
    
    if filename[-4:]=='xlsx':
        df = pd.read_excel(filename)
    elif filename[-3:]=='csv':
        df = pd.read_csv(filename)

    colm_data = df.columns
    colm_data = list(colm_data)
    
    dataframes=df
    field_flag = 1
    def saved_data():
        if field_flag == 1:
            fields.delete(0,'end')
            for data in colm_data:
                fields.insert(END,data)
    # print(colm_data)
    # field_flag=1
    
    if field_flag:
        fields.delete(0,'end')
    for data in colm_data:
        fields.insert(END,data)
    if filename:
       filepath = os.path.basename(filename) 
       os.path.splitext(filepath)
       x = os.path.splitext(filepath)

        

       print(x)
       Button(f2, text=x[0], command=saved_data).pack()   
    elif colm_data:
        colm_data = list
    fields.bind('<Button-3>',pop_up)
      
      
canvas_flag =0
def graph_plot():  
    canvas_flag = 1
    if canvas_flag:
        for rc_value in f5.winfo_children():
            rc_value.destroy()
    
    selected_plot = Select_plot.get()
    
    
    xcol = dataframes[colm_value]
    yrow = dataframes[row_value]
    fig = Figure(figsize= (8,7))
    ax =fig.subplots()
    if selected_plot=='Bar-Graph':
        ax.bar(xcol,yrow)
    elif selected_plot=='Line-Graph':
        ax.plot(xcol,yrow)
    elif selected_plot == 'Pie-Chart':
        ax.pie(yrow)
   
    canvas = FigureCanvasTkAgg(fig, master = f5)
    canvas.draw()
    canvas.get_tk_widget().pack()
root =Tk()
root.title('Project Ocean')
# top.iconbitmap('logo.ico')
root.geometry('1100x650')


# w= root.winfo_screenwidth()
# h=root.winfo_screenheight()
# print(h)
# print(w)
menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="New")  
file.add_command(label="Open")  
file.add_command(label="Save")  
file.add_command(label="Save as...")  
file.add_command(label="Close")  
menubar.add_cascade(label="File", menu=file)  
edit = Menu(menubar, tearoff=0)  
Data = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Data", menu=Data) 
Data.add_command(label="heelo")
worksheet = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Worksheet", menu=worksheet) 
worksheet.add_command(label="heelo")
menubar.add_cascade(label="Dashboard")  
menubar.add_cascade(label="Story")  
menubar.add_cascade(label="Analysis")  
menubar.add_cascade(label="Map")  
menubar.add_cascade(label="Format")  
menubar.add_cascade(label="Server")  
menubar.add_cascade(label="Windows")  
menubar.add_cascade(label="Help", menu=help)  
root.config(menu=menubar) 
path=Frame(root,bg='white',height=40,border=40)
path.pack_propagate(0)

path.pack(side='bottom',fill=X,anchor='s')






f2 =Frame(root,bg='white',width=320,border=3)
f2.pack_propagate(0)
f2.pack(side='left',fill=Y)

btn_frame=Frame(f2,bg='white')
btn_frame.pack(side='top',fill=X)
Btn= Button(btn_frame, text='Data', height=2,width=25, border=3).pack(side='left',padx=1)
Btn= Button(btn_frame, text='Analytics',  height=2,width=30, border=3).pack(side='left',padx=1)
      
Btn1= Button(f2, text='Connect to Data', command=upload_btn,  height=2,width=8, border=3)
Btn1.pack(side='top',fill=X)

Select_plot=StringVar()
Select_plot.set("Select the Plot")

drop = OptionMenu(f2, Select_plot,"Line-Graph","Bar-Graph","Pie-Chart")
drop.pack(side='top',fill=Y)

Btn2= Button(f2, text='Plot', height=2,width=8, border=3,command=graph_plot)
Btn2.pack(side='top',fill=Y)
def pop_up(e):
        menu = Menu(f2, tearoff= 0)
        menu.add_command(label= "Select as Column", command=lambda: CurSelet(e))
        menu.add_command(label= "Select as Row", command= lambda: CurSelect(e))
        menu.add_command(label= "Filter",command=Filter)
        menu.add_separator()
        menu.add_command(label= "quit", command=f2.quit)
        
        menu.tk_popup(e.x_root, e.y_root)
field_flag = 0
scroll_bar = Scrollbar(f2)
scroll_bar.pack(side = RIGHT,fill=Y)


fields = Listbox(f2,width =280 , height=15, yscrollcommand = scroll_bar.set )
fields.pack()
scroll_bar.config( command = fields.yview)




    # for data in canvas.get_children():
    #     canvas.delete(data)
    
def CurSelet(evt):
    global colm_value
    colm_value=str((fields.get(ACTIVE)))
    # print ('this i need as column',value)
    colm_input.config(text = colm_value)
def CurSelect(evt):
    global row_value
    row_value=str((fields.get(ACTIVE)))
   
    # print ('this i need as row',value)   
    row_input.config(text= row_value)
    
# plt.plot(row_input,colm_input)

    
    # print(fields)

        
        
    # def set_colm():
    #      pass
    # def set_row():
    #      pass
     
    
    # fields.bind("<Button-1>",pop_up)



# options= ['Bar graph','','','','','']
# plot_menu = OptionMenu(f2,plot_menu_,*options)

rc_frame=Frame(root,height=50,bg='grey')
rc_frame.pack(side='top',fill=X)

f3 =Frame(root, bg='grey',width=220,border=13)
f3.pack_propagate(0)
f3.pack(side='left',fill=Y)

f5 = Frame(root, bg='white',width=1300,border=12)
f5.pack_propagate(0)
f5.pack(side='left',fill=Y)


column_frame = Frame(rc_frame,bg='grey')
column_frame.pack(side="left",fill=X)
column=Label(rc_frame, text='Column :',height=1,width=8).pack(side='left',fill=X,padx=5,pady=5)
colm_input=Label(rc_frame,text='')
colm_input.pack(side='left',fill=X, padx=5,pady=5)

# Column=StringVar()
# Column.set("Select")
# drop = OptionMenu(rc_frame, Column,"Range","Order").pack(side='left', fill=X,padx=5,pady=5)

row_frame=Frame(f3, bg='grey')
row_frame.pack(side="left",fill = X)
row=Label(rc_frame,text="Row :",height=1,width=8).pack(side='left',fill = X, padx=5,pady=5)
row_input=Label(rc_frame,text='')
row_input.pack(side='left',fill=Y, padx=5,pady=5)

filter_btn=Button(f3,text="Filter",width=8,height = 2,command=Filter)
filter_btn.pack(side='top', fill=Y)


# exclude_btn = Button(f3,text='exclude',command=delete_from_graph).pack()

# filter_btn=Button(winsx,text="filter",command=Filter_pop)
# filter_btn.pack(side='left', fill=Y)





root.mainloop()