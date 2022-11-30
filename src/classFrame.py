import tkinter as tk
from tkinter import ttk

class CustomFrame(tk.Frame):
    def __init__(self, parent, label, items):
        tk.Frame.__init__(self, parent)
        header = tk.Frame(self)
        self.sub_frame = tk.Frame(self, relief="sunken",
                                  width=400, height=22, borderwidth=1)
        header.pack(side="top", fill="x")
        self.sub_frame.pack(side="top", fill="both", expand=True)

        self.var = tk.IntVar(value=0)
        self.label = tk.Label(header, text=label)
        toggle_btn = ttk.Checkbutton(frame, width=2, text='+',
                                     variable=var, style='Toolbutton')
        toggle_btn['command'] = lambda a1=var, a2=toggle_btn, a3=self.sub_frame: self.toggle(a1, a2, a3)

        self.entry = tk.Entry(header, width=11)

        self.label.pack(side="left")
        self.toggle_btn.pack(side="left")
        self.entry.pack(side="right", pady=2, anchor="e")
        self.sub_frame.pack(side="top", fill="both", expand=True)

        for item in items:
            tk.Label(self.sub_frame, text=item).pack(side="top")

        # this sets the initial state
        self.toggle(False)

    def toggle(self, show=None):
        show = self.var.get() if show is None else show
        if show:
            self.sub_frame.pack(side="top", fill="x", expand=True)
            self.toggle_btn.configure(text='-')
        else:
            self.sub_frame.forget()
            self.toggle_btn.configure(text='+')

class Example:
    def __init__(self, root):
        list_1 = ['item_1', 'item_2']
        list_2 = ['a', 'b', 'c']

        for item in list_1:
            frame = CustomFrame(root, item, list_2)
            frame.pack(side="top", fill="x")

if __name__ == '__main__':
    list_1 = ['item_1', 'item_2']
    list_2 = ['a', 'b', 'c']

    root = tk.Tk()

    frames = dict()

    for item in list_1:
        frames[item] = tk.Frame(root)
        frames[item].pack()
        frames[item].labels = dict()
        for text in list_2:
            frames[item].labels[text] = tk.Label(frames[item], text=text)
            frames[item].labels[text].pack()

    root.mainloop()