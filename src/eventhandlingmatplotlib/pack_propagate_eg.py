import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, width=500, height=500)
frame.pack_propagate(0)  # Prevent automatic resizing

label = tk.Label(frame, text="This is a label")
label.pack()

button = tk.Button(frame, text="Click me")
button.pack()

frame.pack()

root.mainloop()
