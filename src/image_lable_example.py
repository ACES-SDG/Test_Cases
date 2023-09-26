import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def show_custom_dialog():
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title("Custom Dialog")

    # Create a custom style with a background color
    custom_style = ttk.Style()
    custom_style.configure("Custom.TFrame", background="lightblue")

    label_frame = ttk.Frame(custom_dialog, style="Custom.TFrame")
    label_frame.pack(pady=10)

    # Load an image for the alert icon (replace 'alert.png' with your image file)
    alert_image = Image.open("C:/Users/Mazhar/OneDrive/Desktop/LIve_Working/practice/my_practice/src/danger.png")  # Replace with the path to your image
    alert_image = alert_image.resize((20, 20), Image.ANTIALIAS)
    alert_icon = ImageTk.PhotoImage(alert_image)

    label = ttk.Label(label_frame, text="Do you want to save changes?", image=alert_icon, compound=tk.LEFT, font=("Helvetica", 12))
    label.image = alert_icon  # Keep a reference to the image
    label.pack(padx=10, pady=5)

    button_frame = ttk.Frame(custom_dialog)
    button_frame.pack(pady=10)

    save_button = ttk.Button(button_frame, text="Save", command=save_changes)
    dont_save_button = ttk.Button(button_frame, text="Don't Save", command=dont_save_changes)
    cancel_button = ttk.Button(button_frame, text="Cancel", command=custom_dialog.destroy)

    save_button.grid(row=0, column=0, padx=10)
    dont_save_button.grid(row=0, column=1, padx=10)
    cancel_button.grid(row=0, column=2, padx=10)

def save_changes():
    print("Saving changes...")

def dont_save_changes():
    print("Discarding changes...")

root = tk.Tk()
root.title("Custom Message Box")

ask_button = ttk.Button(root, text="Ask", command=show_custom_dialog)
ask_button.pack(pady=20)

root.mainloop()
