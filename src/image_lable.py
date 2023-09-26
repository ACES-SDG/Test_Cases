import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()

# Create a PhotoImage object (replace 'your_image.png' with the path to your image file)
image = PhotoImage(file='src\home.png')

# Create a button with text and an image
button = tk.Button(root, text="Click Me", image=image, compound=tk.LEFT)
button.pack()

root.mainloop()
