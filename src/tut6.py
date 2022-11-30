from tkinter import *

root = Tk()
root.geometry("444x266")
root.title("MAZHAR")

# important label option
# text - for adding text
# bd - for background
# fg - foreground
# font - sets the font
# font=("Timees New Roman",14, "bold")
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
title_label = Label (text=''' Mirzā Mazhar Jān-i Jānān (Urdu: مرزا مظہر جانِ جاناں), also known by his laqab Shamsuddīn \nHabībullāh (1699–1781), was a renowned Hanafi Maturidi Naqshbandī Sufi poet of Delhi, distinguished as one of the "four \npillars of Urdu poetry."[1] He was also known to his contemporaries as the sunnītarāsh, "Sunnicizer", for his absolute, \nunflinching commitment to and imitation of the Sunnah. ''', bg="lightBlue", fg="violet", padx=24, pady=32, font="Arial 14 bold", borderwidth=3, relief=SUNKEN )

# important pack options
# anchor = nw,ne,se,sw
# side= TOP, BOTTOM, LEFT,RIGHT
# fill
# padx
# pady


title_label.pack(side=BOTTOM,anchor="sw", fill=X)

root.mainloop()
