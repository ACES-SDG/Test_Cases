from tkinter.tix import *
from tkinter import *
from tkinter import tix
from PIL import Image, ImageTk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,
    NavigationToolbar2Tk
)


def btn_hover(side,set_frame,bcolor,fcolor,text): #,msg_,tip1
    
    def on_btn(e):
        our_btn["bg"] = bcolor
        our_btn["fg"] = fcolor
        
    def off_btn(e):
        our_btn["bg"] = fcolor
        our_btn["fg"] = bcolor
        
    our_btn =Button(master=set_frame,width=30,height=30,
                    text=text,
                    fg=bcolor,
                    bg=fcolor,
                    border=0,
                    activeforeground=fcolor,
                    activebackground=bcolor,
                    command='')
    our_btn.bind("<Enter>",on_btn)
    our_btn.bind("<Leave>",off_btn)
    # tip1.bind_widget(our_btn, balloonmsg=msg_)
    
    our_btn.pack(side=side,padx=5,pady=2)