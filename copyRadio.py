import tkinter as tk

import customtkinter as ctk

def dec(func):
    def execuNow(self):
        print('excuting')
        func(self)
        print('executed')
    return execuNow
class MyRadioButtons(tk.Frame):
    def __init__(self, parent=None, items=[]):
        tk.Frame.__init__(self, parent)

        global list_of_items, var
        list_of_items= items
        
        var = tk.IntVar()

        for index,item in enumerate(items):

            radio_button = ctk.CTkRadioButton(self,variable=var,text=item,value=index,command=self.sel)
            radio_button.pack(side=tk.LEFT,fill='x',padx=10,pady=15)
            radio_button.config(fg_color='darkblue',text_color='black',hover_color= 'black')

            radio_button.bind("<Enter>", self.on_enter)
            radio_button.bind("<Leave>", self.on_leave)

    def on_enter(self,event):
        event.widget.config(text_color='green')
    
    def on_leave(self,event):
        event.widget.config(text_color='black')

   
    @dec
    def sel(self):
        # global selected_item
        """  returns the selected radio button as string  """
        # print("You selected  " + str(var.get()))
        # print('\n it is ',list_of_items[var.get()],'\n')
        # print(list_of_items)
        selected_item  =list_of_items[var.get()]
        print(f"I'm in sel function now , selected option is {selected_item}")
        # return selected_item

        
    def return_item(self):
        # try:
        #     if bool(selected_item):
        #         return selected_item
        # except:
        return self.sel()
        


root = tk.Tk()

frame = tk.Frame(root,height=100,width=100,bg='lightblue')
frame.pack(side='left')

choices = ['Year','Quarter','Month','Week']

obj = MyRadioButtons(frame,choices)
obj.pack()

item  = obj.return_item()
print(item)
root.mainloop()