import random
import time
import os
import sys
import tkinter as tk
from tkinter import ttk
####################


def SliderUpdate(z):
    Z = DwarfSlide.get()#gets the current value of the dwarf slider (1 - 100)
    a = oneSlide.get()#gets the current value of the one slider (1-100)
    onelabel.configure(text=a)#changes the text of the labels to what the sliders currently are
    DwarfValuelabel.configure(text=Z)
    
    PercentSpent = Z + a#adds the two percentages together in order to find out what has been spent (if  one == 30 and dwarf == 40, then 70% will have already been used
    totalPercentLeft = 100 - PercentSpent#how much is yet to be used by the sliders

    dwarfUpdate = Z + totalPercentLeft#gets a value so that the slider can be updated to give a new maximum value
    DwarfSlide.configure(to=dwarfUpdate)#updates the slider with the new maximum value

    oneUpdate = a + totalPercentLeft
    oneSlide.configure(to=oneUpdate)

    
    DwarfDecim = Z/100
    oneDecim = a/100
    DwarfPop = DwarfDecim*TotalValue
    DwarfPop = int(DwarfPop)
    onePop = oneDecim*TotalValue
    onePop = int(onePop)
    totalPop = onePop + DwarfPop#used to check if accurate results are being given

    print("one Population is: ", onePop ,",   Dwarf Population is:  ", DwarfPop, "   Original total Population is;   ", TotalValue, "   and new total population is;     ", totalPop)



global TotalValue#Total value is a User input for the population of a city  - it can be any value
TotalValue = 1000


global CalibrateWin
CalibrateWin = tk.Tk()#creates a new window for the Calibration section
CalibrateWin.title('RCG 3.1')
CalibrateWin.configure(bg='#D8BFD8')
Calib_w = 600
Calib_h = 400
screen_w = CalibrateWin.winfo_screenwidth()
screen_h = CalibrateWin.winfo_screenheight()
centre_x = int(screen_w/2 - Calib_w/2)
centre_y = int(screen_h/2 - Calib_h/2)
CalibrateWin.geometry(f'{Calib_w}x{Calib_h}+{centre_x}+{centre_y}')#centres on every screen

DwarfVar = tk.DoubleVar()
DwarfSlide = tk.Scale(CalibrateWin, from_=1, length =100, to=100, orient='horizontal', variable=DwarfVar, command=SliderUpdate, resolution = 1, showvalue = 0)#creates a scale on the calibrate window from the range 1 - 100, with a horizontal orientation, and will trigger the 'SliderUpdate subroutine when moved)
DwarfSlide.place(x=150, y=70)
DwarfSlide['state'] = 'normal'#prevents it from being half clicked when created
DwarfValuelabel = tk.Label(CalibrateWin, text="-")#this label will be updated with what the percentage currently is
DwarfValuelabel.place(x=10, y=70)

oneVar = tk.DoubleVar()#same code as above but for a second variable
oneSlide = tk.Scale(CalibrateWin, from_=1, length =100, to=100, orient='horizontal', variable=oneVar, command=SliderUpdate, resolution = 1, showvalue = 0)
oneSlide.place(x=150, y=100)
oneSlide['state'] = 'normal'
onelabel = tk.Label(CalibrateWin, text="-")
onelabel.place(x=10, y=100)