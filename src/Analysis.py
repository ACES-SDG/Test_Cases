import tkinter as tkk
from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt


def analyze(root, df):
    listbox =  Listbox(root,
                       height= 50,
                       width= 20,
                       bg="lightgray",
                       fg="black",
                       font = "Helvetica"
                       )
    listbox.insert(list(df.columns))
    listbox.pack()
    

