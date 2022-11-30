from tkinter import  GROOVE, LEFT, TOP, X, Y, Button, Label, Tk
from tkinter.filedialog import askopenfilename
from customtkinter import CTkFrame
import pandas as pd


# import datetime
# import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd 
# import numpy as np
# N=3
# # from collections import Counter

# df = pd.read_excel("C:/Users/acesi/OneDrive/Desktop/Excel_files/Sample - Superstore2.xlsx")
# # colors = np.random.rand(N)

# # print(df.columns)
# # dates = list(df['Order Date'])
# # df['year']=df['Order Date'].dt.year

# # print(df['Order Date'].dt.year.unique())

# sales_by_year = df.groupby([df['Order Date'].dt.year,'Category']).aggregate({'Sales':sum})

# # sales_by_year = df.groupby('Order Date').agg({'Sales':sum})




# df.pivot_table(index='col1', columns='col2', values='col3',
            #    aggfunc=['sum','count'])

# print(list(sales_by_year['Sales']))
# y = list(sales_by_year['Sales'])

# x_dict = dict(sales_by_year)
# x_y = dict(x_dict['Sales'])
# x =list(x_y.keys())
# print(x,y)
# plt.bar(x, y)
# plt.xticks(x)

# plt.connect('button_press_event',lambda event: print(event.xdata))

# plt.scatter('Order Date', 'Sales',data=sales_by_year, s='Profit', c=colors, alpha=0.5,sizes=(200,1000))
# plt.show()
# print(sales_by_year)
# years=[]
# for i in dates:
#     year_ = i.year
#     years.append(year_)

# years_2 = []
# def c(*i):
#     years_2.append(i.year)
# c(*dates)
# # print(*Counter(years_2),'2nd \n')

# print(*Counter(years),' 1st \n')


# ============================================= MAP =========================================================

def labl_h(text):
    labels = Label(top_hedings,text=text,width=12,borderwidth=3,)
    labels.pack(side=LEFT,padx=2)

def labl_sh(text):
    labels = Label(side_headings,text=text,borderwidth=3,anchor='w',width=12)
    labels.pack(pady=2)


def t_cal(h,sh,sales):
    global main_f,top_hedings,side_headings

    top_hedings = CTkFrame(main_f,height=50, )
    top_hedings.pack(side=TOP,fill=X)

    top_box = CTkFrame(top_hedings, width=98,height=50)
    top_box.pack(anchor='nw',side=LEFT)

    side_headings = CTkFrame(main_f, width=100)
    side_headings.pack(side=LEFT,fill=Y,anchor='nw',padx=2)

    list(map(labl_h,h))
    list(map(labl_sh,sh))


    
def openfile():
    global cols
    btn = askopenfilename(initialdir="Desktop",
                                          title="Select A File",
                                          filetype=(('text files','*.csv'),("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    df= pd.read_csv(btn)
    df['Order Date']= pd.to_datetime(df['Order Date'])

    h = df['Category'].unique()
    # lsit_ = list(df['Order Date'].dt.year.unique())
    # h = sorted(df['Order Date'].dt..unique())

    sh = sorted(df['Sub-Category'].unique())
    # print(sh)
    sales_by_year = df.groupby(['Category','Sub-Category']).aggregate({'Sales':sum})

    t_cal(h,sh,sales_by_year)


listofu = []



app = Tk()

screen_width = app.winfo_screenwidth()
btn =Button(command=openfile,text='open file',height=2,bg='blue',fg='yellow',borderwidth=3,relief=GROOVE)
btn.pack(side=TOP)


main_f =CTkFrame(app,borderwidth=3,width=750,height=556,border_color='black')
main_f.pack_propagate(0)
main_f.pack(side=TOP)




app.mainloop()