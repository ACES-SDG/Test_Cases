from tkinter import Tk
import tkinter.messagebox as msgbox


def display_msg():
    msgbox.showinfo(title='', message='Thank You')
    root.destroy()


root = Tk()

root.protocol('WM_DELETE_WINDOW', display_msg)

root.mainloop()