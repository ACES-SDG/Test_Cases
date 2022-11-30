import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

file_path = ''
def set_file_path(path):
    global file_path
    file_path = path


"""
method name: run 
run method is to execute the code which is been given in the app 
"""
def run():
    code = editor.get('1.0',END)
    exec(code)

"""
method name: save_as 
save_as method is used to save the file to .py extention with the code 
block written in it.
"""
def save_as():
    if file_path== '':
        path = asksaveasfilename(filetypes=[('python files','*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0',END)
        file.write(code)



"""
medthod name: open_file
open_file mehtod is used to open the existing file of .py exctention.
"""
def open_file():
    path = askopenfilename(filetypes=[('python files','*.py')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)

"""
Tkinter main window for the compiler app 
"""
Compiler = Tk()
Compiler.title('My Compiler')

menu_bar = Menu(Compiler)  # creating the  menu bar

file_menu = Menu(menu_bar, tearoff=0)
#  submmenus for file menu 
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=None)
file_menu.add_command(label='Save as',command=save_as)
file_menu.add_command(label='Exit',command=exit)

menu_bar.add_cascade(label='File',menu=file_menu) # file menu 


run_bar =Menu(menu_bar,tearoff=False) # adding run menu bar in menu bar 
run_bar.add_command(label='Run',command=run) # adding sub menu to it
menu_bar.add_cascade(label='Run',menu=run_bar)
Compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

Compiler.mainloop()