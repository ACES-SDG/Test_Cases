import tkinter as tk
from typing import List


class ChecklistBox(tk.Frame):
    def __init__(self,  choices=[], ):
        tk.Frame.__init__(self, )

        self.vars = []
        bg = self.cget("background")
        for choice in choices:
            var = tk.StringVar(value=choice)
            self.vars.append(var)
            cb = tk.Checkbutton(self, var=var, text=choice,
                                onvalue=choice, offvalue="",
                                anchor="w", width=20, background=bg,
                                relief="flat", highlightthickness=0
            )
            cb.pack(side="top", fill="x", anchor="w")


    def getCheckedItems(self):
        values = []
        for var in self.vars:
            value =  var.get()
            if value:
                values.append(value)
        return values
root = tk.Tk()
choices = ["Author", "John", "Mohan", "James", "Ankur", "Robert"]
checklist = ChecklistBox(root, choices)

print("choices:", checklist.getCheckedItems())

tk.mainloop()
