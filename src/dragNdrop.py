
from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX= event.x
    widget.startY= event.y

def drag_motion(event):
    widget = event.widget
    x= widget.winfo_x() - widget.startX + event.x
    y= widget.winfo_y() - widget.startY + event.y
    widget.place(x=x,y=y)

window = Tk()

label1 =Label(window, bg='red', width=10, height=5,cursor='fleur')
label1.place(x=1,y=1)

label2 =Label(window, bg='blue', width=10, height=5)
label2.place(x=100, y=100)

label1.bind("<Button-1>",drag_start)
label1.bind("<B1-Motion>",drag_motion)

window.mainloop()