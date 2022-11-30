from tkinter import PhotoImage
from tkinter import *
from tkinter.tix import Balloon
from turtle import screensize
from PIL import Image, ImageTk
from Buttons import btn_hover


def callFrame_menuiconbar(self):
    
    home_icon              = PhotoImage(file="home.png")    
    img = ImageTk.PhotoImage(Image.open("photo.jpg"))                
    back_icon              = PhotoImage(file="back_arrow.png")             
    next_icon              = PhotoImage(file="next_arrow.png")
    undo_icon              = PhotoImage(file="undo.png")
    save_icon              = PhotoImage(file="save.png")
    add_database_icon      = PhotoImage(file="add_data.png")
    refresh_icon           = PhotoImage(file="refresh.png")
    add_sheet_icon         = PhotoImage(file="add_sheet.png")
    copy_sheet_icon        = PhotoImage(file="copy_sheet.png")
    clear_sheet_icon       = PhotoImage(file="clear_sheet.png")
    sort_ascending_icon    = PhotoImage(file="sort_ascending.png")
    sort_descending_icon   = PhotoImage(file="sort_descending.png")
    highlight_icon         = PhotoImage(file="highlight.png")
    group_members_icon     = PhotoImage(file="group_members.png")
    show_mark_label_icon   = PhotoImage(file="show_mark_label.png")
    fix_axis_icon          = PhotoImage(file="fix_axis.png")
    show_hide_cards_icon   = PhotoImage(file="show_hide_cards.png")
    presentation_mode_icon = PhotoImage(file="presentation_mode.png")
    share_icon             = PhotoImage(file="share.png")
    new_dashboard_icon     = PhotoImage(file="new_dashboard.png")
    story_icon             = PhotoImage(file="story.png")
    new_sheet_icon         = PhotoImage(file="new_sheet.png")

    screen_width=self.winfo_screenwidth()
    menu_icon_bar = Frame(self, borderwidth=6, bg='#f9f9f9', relief=GROOVE,width=screen_width, height=30)
    menu_icon_bar.pack_propagate(0)

    menu_icon_bar.pack(side=TOP, anchor="nw", fill=X)

    btn_hover(LEFT, menu_icon_bar,  "yellow", "red",'abcd')
    btn_hover(LEFT, menu_icon_bar,  "yellow", "red",'abcd')
    
    
    pass