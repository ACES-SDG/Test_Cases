import os
import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
import sys
from tkinter import ttk


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def show_custom_dialog():
    global selected_button
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title("ACES Analytics tool")   
    
        
    # Center the splash screen on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - 400) // 2
    y_position = (screen_height - 300) // 2
    custom_dialog.geometry(f"450x170+{x_position}+{y_position}")
    custom_dialog.resizable(False, False)
    
    # print(custom_dialog.winfo_height(custom_dialog))
    
    up = ctk.CTkFrame(custom_dialog,fg_color='white',height=90,width=450)
    up.pack_propagate(0)
    up.pack(side='top')
    
     # Load an image for the alert icon (replace 'alert.png' with your image file)
    # alert_image = Image.open("C:/Users/Mazhar/OneDrive/Desktop/LIve_Working/practice/my_practice/src/danger.png")  # Replace with the path to your image
    # alert_image = alert_image.resize((40, 40), )
    # alert_icon = ImageTk.PhotoImage(alert_image)
    
    image_path = resource_path("test_images")
    
    alert_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "danger.png")), size=(45, 45))
    
    alert_lable = ctk.CTkLabel(up, image=alert_image,compound=tk.LEFT,text = None)
    alert_lable.pack(side = 'left',padx = (20,10))
    
    label = ctk.CTkLabel(up, text="Do you want to save changes to 'My work.owbx'? \n ",  font=("Inter", 15))
    label.pack(pady=(25,10), side = 'left')
    
    button_frame = ctk.CTkFrame(custom_dialog, fg_color='#e9e9e9',height=80,width=450)
    button_frame.pack_propagate(0)

    button_frame.pack(side="top")

    save_button = ctk.CTkButton(button_frame, text="Save",width=100,
                                fg_color='#213966',text_color='white',
                                hover_color='#7696D0',command=lambda : save_changes(save_button))
    selected_button = save_button
    dont_save_button = ctk.CTkButton(button_frame, text="Don't Save", 
                                     command=lambda : dont_save_changes(dont_save_button),
                                     width=100,fg_color='white',text_color='black',
                                hover_color='#7696D0',)
    cancel_button = ctk.CTkButton(button_frame, text="Cancel",width=100,
                                  fg_color='white',text_color='black',
                                hover_color='#7696D0',  
                                command=lambda : close(custom_dialog,cancel_button),
                                )

    # save_button.grid(row=0, column=0, padx=(20,5))
    cancel_button.pack(side="right",padx=(0,15))
    
    dont_save_button.pack(side="right",padx=(0,15))
    # dont_save_button.grid(row=0, column=1, padx=(0,5))
    
    # cancel_button.grid(row=0, column=2, padx=(0,5))
    save_button.pack(side="right",padx=(0,15))
    
def toggle_button(button):
    global selected_button
    if selected_button:
        # Deselect previous button, change back to white
        selected_button.configure(fg_color='white',text_color='black',)

    if selected_button is not button:  # If clicking a different button
        # Select current button, change to red
        button.configure(fg_color='#213966',text_color='white',)

        selected_button = button

    else:
        selected_button = None  # Deselect current button
def save_changes(btn):
    toggle_button(btn)
    
    print("Saving changes...")

def dont_save_changes(btn):
    toggle_button(btn)
    
    print("Discarding changes...")
    
def close(window, btn):
    toggle_button(btn)
    
    window.destroy()

root = tk.Tk()
root.title("Custom Message Box")

ask_button = ttk.Button(root, text="Ask", command=show_custom_dialog())
ask_button.pack(pady=20)

root.mainloop()
