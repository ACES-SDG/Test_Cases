import tkinter as tk
from tkinter import ttk

def show_custom_dialog():
    custom_dialog = tk.Toplevel(root)
    custom_dialog.title("Custom Dialog")

    # Create a style for the frame
    style = ttk.Style()
    style.configure("Custom.TFrame", background="lightblue")  # Set the background color

    # Create a frame with the custom style
    frame = ttk.Frame(custom_dialog, style="Custom.TFrame")
    frame.pack(pady=10)

    label = ttk.Label(frame, text="Do you want to save changes?", font=("Helvetica", 12))
    label.pack(pady=10)

    button_frame = ttk.Frame(frame)
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
