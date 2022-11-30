from tkinter import *
from classz import *

users=['Anne', 'Bea', 'Chris', 'Bob', 'Helen']


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[]):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack()
            self.vars.append(var)
    def check(self):
        lst=list(map((lambda var: var.get()), self.vars))
        nlst=[u for l,u in zip(lst,users) if l==1]
        return nlst


root = Tk()

f = Frame(root,height=200,width=200,bg='yellow')
f.pack_propagate(0)
f.pack(side=TOP)
lng = Checkbar(f, users)
lng.pack()

def allstates(): 
  print(lng.check())
#   root.quit()

b=Button(root, text='Check', command=allstates)
b.pack()
root.mainloop()