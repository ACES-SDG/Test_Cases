from tkinter import *
from tkinter.filedialog import askopenfilename

import pandas as pd




class MyTable(Frame):
    def __init__(self, parent=None, items=[]):
        
        def del_x(w,n):
            print(n)
            print(w)
            pass

        def menu(e):
            Widget =e.widget
            name = e.widget.cget('text')
            dash_m = Menu(self, tearoff = 0)

            dash_m.add_command(label ="Delete Sheet",command=lambda: del_x(Widget,name))
            try:
                dash_m.tk_popup(e.x_root, e.y_root)
            finally:
                dash_m.grab_release()

        
        Frame.__init__(self,parent)

        for item in items:
            headerBtn = Button(self,text=item,relief=GROOVE,bg='white',width=10)
            headerBtn.pack(side=LEFT,padx=1,anchor='w')
            headerBtn.bind('<Button-3>',menu)
        pass
    pass

def openfile():
    global cols
    btn = askopenfilename(initialdir="Desktop",
                                          title="Select A File",
                                          filetypes=(('text files','*.csv'),("xlsx files", "*.xlsx"), ("All Files", "*.*")))
    df= pd.read_csv(btn)
    
    cols = df.columns

    tabl = MyTable(table_head,cols)
    tabl.pack(side=LEFT)

    rows = []
    for i in range(len(df)):
        row = df.iloc[i]
        rows.append(row)

        table_body = Frame(height=30,width=screen_width,bg='red')
        table_body.pack()

        tabl_b = MyTable(table_body,row)
        tabl_b.pack(side=LEFT)
        


app = Tk()

screen_width = app.winfo_screenwidth()
btn =Button(command=openfile,text='open file',height=2,bg='blue',fg='yellow',borderwidth=3,relief=GROOVE)
btn.pack(side=TOP)

table_head = Frame(height=30,width=screen_width,bg='yellow')
table_head.pack()





app.geometry('1300x750')
app.title('Ocean Desktop Beta')
app.minsize(1200, 650)
app.mainloop()