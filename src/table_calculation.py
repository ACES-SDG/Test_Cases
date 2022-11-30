from math import floor
from tkinter import  GROOVE, LEFT, TOP, X, Y, Button, Frame, Label, Tk
from tkinter.filedialog import askopenfilename
from customtkinter import CTkFrame,CTkLabel
import pandas as pd





def t_cal(h,sh,sales):
    global main_f
    my_list=[]
    
    def ele():
        def hover_enter(e):
            e.widget.configure(fg='yellow')
            e.widget.configure(background='red')

        def hover_leave(e):
            e.widget.configure(background='white')
            e.widget.configure(fg='black')

        listk = dict(sales['Sales'])
        x = list(listk.keys())
        for i in h:
            side_headings2 = CTkFrame(main_f, width=98)
            side_headings2.pack(side=LEFT,fill=Y,anchor='nw',padx=2)

            # list_h = []
            for j in sh:
                labels_ = Label(side_headings2,text='  ', bg='white',borderwidth=2,width=12)
                labels_.pack(pady=2)
                labels_.bind('<Enter>',hover_enter)
                labels_.bind('<Leave>',hover_leave)
                
               
                for k in x:
                    if i in k and j  in k:
                        # print(f'{i} , {j} are in {k} and its sales per year is {listk[k]}')

                        labels_.configure(text=floor(listk[k]))
                        # my_list.append(listk[k])
                        # labels = Label(side_headings2,text=floor(listk[k]),borderwidth=3,width=12)
                        # labels.pack(pady=2)
                    else:
                        # empty=' '
                        # my_list.append(empty)
                        pass


                        # labels = Label(side_headings2,text='',borderwidth=3,width=12)
                        # labels.pack(pady=2)
        print(my_list,'\n',len(my_list))
        

    btn =Button(command=ele,text='clcik me ',height=2,bg='blue',fg='yellow',borderwidth=3,relief=GROOVE)
    btn.pack(side=TOP)


    # def elements(k):
    #     labels = Label(side_headings2,text=int(k),borderwidth=3,width=12)
    #     labels.pack(pady=2)
   
        # pass

    top_hedings = CTkFrame(main_f,height=50, )
    top_hedings.pack(side=TOP,fill=X)

    top_box = CTkFrame(top_hedings, width=98,height=50)
    top_box.pack(anchor='nw',side=LEFT)

    side_headings = CTkFrame(main_f, width=100)
    side_headings.pack(side=LEFT,fill=Y,anchor='nw',padx=2)

    for i in h:
        # frame_h = CTkFrame(top_hedings,border_width=2,border_color='black')
        # frame_h.pack(side=LEFT,padx=2)
        labels = Label(top_hedings,text=i,width=12,borderwidth=2)
        labels.pack(side=LEFT,padx=2,)#pady=2

    for j in sh:
        # frame_sh = CTkFrame(side_headings,border_width=2,border_color='black')
        # frame_sh.pack(pady=2)
        labels = Label(side_headings,text=j,borderwidth=2,anchor='w',width=12)
        labels.pack(pady=2) #,padx=2

    numlsit = list(sales['Sales'])
    print(numlsit)

    
    
    
    
    # for n in range(len(h)):
        
    #     count =0
    #     for k in numlsit:

            
            
    #         labels = Label(side_headings2,text=int(k),borderwidth=3,width=12)
    #         labels.pack(pady=2)

    #         count +=1
            
    #         # print(n,count)
    #         if count==len(sh):
    #             del numlsit[0:3]         
    #             break
    
def openfile():
    global cols
    btn = askopenfilename(initialdir="Desktop",
                                          title="Select A File",
                                          filetype=(('text files','*.csv'),("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    df= pd.read_csv(btn)
    df['Order Date']= pd.to_datetime(df['Order Date'])
    
    cols = df.columns
    # print(df['Order Date'])


    # h = df['Category'].unique()
    # lsit_ = list(df['Order Date'].dt.year.unique())
    h = sorted(df['Order Date'].dt.year.unique())

    sh = sorted(df['Sub-Category'].unique())
    # print(sh)
    sales_by_year = df.groupby([df['Order Date'].dt.year,'Sub-Category']).aggregate({'Sales':sum})
    # print(sales_by_year)
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