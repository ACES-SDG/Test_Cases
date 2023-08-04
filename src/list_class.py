import tkinter as tk


class MyListBox(tk.Listbox):

    def __init__(self, master=None, *args, **kwargs):
        tk.Listbox.__init__(self, master, *args, **kwargs)

        self.bg = "white"
        self.fg = "black"
        self.hover_bg = "lightblue"
        self.hover_fg = "black"

        self.current = -1  # current on_hover item

        self.add_items()

        self.bind("<Motion>", self.on_hover)
        self.bind("<Leave>", self.off_hover)

    def add_items(self, item_list=[]):
        """Fills the listbox with some numbers"""
        for i,j in enumerate(item_list):
            self.insert(tk.END, j)
            self.itemconfig(i, {"bg": self.bg})
            self.itemconfig(i, {"fg": self.fg})

    def default_colors(self):
        """Resets the colors of the items"""
        for i,item in enumerate(self.get(0, tk.END)):
            self.itemconfig(i, {"bg": self.bg})
            self.itemconfig(i, {"fg": self.fg})

    def set_on_hover_item(self, index):
        """Set the item at index with the on_hover colors"""
        self.itemconfig(index, {"bg": self.hover_bg})
        self.itemconfig(index, {"fg": self.hover_fg})    

    def on_hover(self, event):
        """Calls everytime there's a motion of the mouse"""
        index = self.index("@%s,%s" % (event.x, event.y))
        if self.current != -1 and self.current != index:
            self.default_colors()
            self.set_on_hover_item(index)
        elif self.current == -1:
            self.set_on_hover_item(index)
        self.current = index

    def off_hover(self, event):
        self.default_colors()
        self.current = -1

