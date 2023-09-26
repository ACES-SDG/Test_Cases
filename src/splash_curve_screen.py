import tkinter as tk
from tkinter import ttk
import time

# Create the main application window
root = tk.Tk()
root.title("Main Application")

# Function to close the splash screen
def close_splash():
    splash_window.destroy()

# Create a splash screen window
splash_window = tk.Toplevel(root)
splash_window.title("Splash Screen")

# Customize the splash screen window
splash_window.geometry("400x300")
splash_window.attributes("-topmost", True)  # Ensure it's on top
splash_window.overrideredirect(True)  # Remove window decorations (title bar, close button)

# Create a Canvas widget for drawing the background with curved edges
canvas = tk.Canvas(splash_window, width=400, height=300)
canvas.pack()

# Create a rounded rectangle
radius = 20
x1, y1, x2, y2 = 10, 10, 390, 290
canvas.create_arc(x1, y1, x1 + 2 * radius, y1 + 2 * radius, start=90, extent=90, fill="blue")
canvas.create_arc(x2 - 2 * radius, y1, x2, y1 + 2 * radius, start=0, extent=90, fill="blue")
canvas.create_arc(x1, y2 - 2 * radius, x1 + 2 * radius, y2, start=180, extent=90, fill="blue")
canvas.create_arc(x2 - 2 * radius, y2 - 2 * radius, x2, y2, start=270, extent=90, fill="blue")
canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill="blue")
canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill="blue")

# After a delay, close the splash screen and show the main application window
root.after(3000, close_splash)  # Delay in milliseconds (3000 ms = 3 seconds)

# Start the main application
root.mainloop()
