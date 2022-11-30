import tkinter as tk


class MyCheckList(tk.Frame):
    def __init__(self, parent=None, items=[]):
        tk.Frame.__init__(self, parent)
        global list_to_filter,box
        list_to_filter = items
        self.vars = []
        for item in items:
            var = tk.IntVar()
            box = tk.Checkbutton(self, text=item, variable=var,cursor='hand2')
            box.bind("<Enter>", self.on_enter)
            box.bind("<Leave>", self.on_leave)


            box.pack(anchor='w',padx=40)
            self.vars.append(var)
    def on_enter(self,event):
        event.widget.config(fg='green')
    
    def on_leave(self,event):
        event.widget.config(fg='black')

    def filter(self):
        lst=list(map((lambda var: var.get()), self.vars))
        filtered_list=[u for l,u in zip(lst,list_to_filter) if l==1]
        # print(f"i'm in checkllist.py and this the value of lst:{lst} and \n this is the value of list to filter:{filtered_list}")
        return filtered_list

root = tk.Tk()

frame = tk.Frame(root,height=100,width=100,bg='lightblue')
frame.pack(side='left')

choices = ["Author", "John", "Mohan", "James", "Ankur", "Robert"]

obj = MyCheckList(frame,choices)
obj.pack(side="left")
root.mainloop()