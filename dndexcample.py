from tkinter import *
from tkinterdnd2 import *
from tkinter.dnd import dnd_start



def dragging(event):
    dnd_start(txt,event)
    

def show_text(event):
    textarea.delete("1.0","end")
    textarea.insert("end",f"{event.widget.cget()}\n")
    
    # if event.data.endswith(".txt"):
    #     with open(event.data, "r") as file:
    #         for line in file:
    #             line=line.strip()
    #             textarea.insert("end",f"{line}\n")

ws = TkinterDnD.Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#fcb103')


frame2 = Frame(ws,width=40,height=10, bg='yellow')
frame2.pack(side=TOP)

frame = Frame(ws)
frame.pack(side=TOP)
textarea = Text(frame, height=18, width=40)
textarea.pack(side=LEFT)
textarea.drop_target_register(DND_ALL)
textarea.dnd_bind('<<Drop>>', show_text)


# textarea.dnd_accept

txt  =  Label(frame2, height=1 )
txt.pack(side=TOP)


txt.bind("<ButtonPress>",dragging)



sbv = Scrollbar(frame, orient=VERTICAL)
sbv.pack(side=RIGHT, fill=Y)

textarea.configure(yscrollcommand=sbv.set)
sbv.config(command=textarea.yview)



ws.mainloop()