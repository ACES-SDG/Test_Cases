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
# You can add your own content or an image to the splash screen here.

# Center the splash screen on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - 400) // 2
y_position = (screen_height - 300) // 2
splash_window.geometry(f"400x300+{x_position}+{y_position}")

# After a delay, close the splash screen and show the main application window
root.after(3000, close_splash)  # Delay in milliseconds (3000 ms = 3 seconds)

# Start the main application
root.mainloop()
