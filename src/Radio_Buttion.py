import tkinter as tk


# class RadioButton(tk.Frame):
#     def __init__(self, options=[]):
#         tk.Frame.__init__(self,options=[])

#         self.vars = []

#         for index,option in enumerate(options):
#             var = tk.IntVar()
#             # self.vars.append(var)
            

#     def sel(self):
#         selection = "You selected the option " + str(self.var.get())

#         print(selection)

def sel(e):
    print(f'You selected the option {e[0].get()}')
root = tk.Tk()
choices = ["Author", "John", "Mohan", "James", "Ankur", "Robert"]
# obj = RadioButton(root,options= choices)
var={}
# var = tk.IntVar()

for index,item in enumerate(choices):
    var[index] = tk.StringVar()

    radio_button = tk.Radiobutton(root,variable=var[index],text=item,value=index+1,command= lambda : sel(var))
    radio_button.pack(side=tk.TOP,fill='x')
tk.mainloop()






# from tkinter import *
# def sel():
#    selection =  str(var[0].get())
#    label.config(text = selection)

# root = Tk()
# var={}
# label = Label(root)
# label.pack()
# # for i in range(0,4):  
# var[i] = StringVar()
# R1 = Radiobutton(root, text="Bad", variable=var[i], value="bad",command=sel)
# R1.select()
# label.config(text=var[i].get())
# R1.pack()
# R2 = Radiobutton(root, text="No Effect", variable=var[i], value="no effect",command=sel)
# R2.pack()
# R3 = Radiobutton(root, text="Good", variable=var[i], value="good",command=sel)
# R3.pack()

# root.mainloop()