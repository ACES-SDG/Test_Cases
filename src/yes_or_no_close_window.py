import tkinter as tk
from tkinter import messagebox

def on_closing():
    result = messagebox.askyesno("Confirmation", "Do you want to close this window?")
    if result:
        root.destroy()

root = tk.Tk()
root.title("Close Confirmation")

# Create a label and a button for demonstration
label = tk.Label(root, text="Close this window:")
label.pack()

close_button = tk.Button(root, text="Close", command=on_closing)
close_button.pack()

# Intercept the window's close button
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
