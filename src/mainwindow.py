# Multi-frame tkinter application v2.2
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.tix import Balloon
from menu_icon_bar import callFrame_menuiconbar
def ask_qus(self):
    val = messagebox.askquestion("Exit?", "Do you want to exit?")
    if val == 'yes':
        self.destroy()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        
        callFrame_menuiconbar(self)
       
        start_label = tk.Label(self, text="This is the start page")
        page_1_button = tk.Button(self, text="Open page one",
                                  command=lambda: master.switch_frame(PageOne))
        
        start_label.pack(side="top", fill="x", pady=10)
        page_1_button.pack()


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        page_1_label = tk.Label(self, text="This is page one")
        start_button = tk.Button(self, text="Return to start page",
                                 command=lambda: master.switch_frame(StartPage))
        page_1_label.pack(side="top", fill="x", pady=10)
        start_button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()