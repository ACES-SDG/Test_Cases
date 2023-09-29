import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Tkinter window
root = tk.Tk()
root.title("Matplotlib in Tkinter")

# Create a Matplotlib figure and a Tkinter Canvas widget
fig = Figure(figsize=(5, 4), dpi=100)

# Create a Matplotlib Axes object
ax = fig.add_subplot(111)

new_data = [22, 33,42, 10]
ax.bar([12, 24, 33, 42], new_data)
    
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()



# Function to clear the plot and draw a new one
def update_plot():
    # Clear the previous plot
    ax.clear()
    
    # Plot new data
    new_data = [2, 3, 4, 1]
    ax.plot([1, 2, 3, 4], new_data)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_title('New Matplotlib Plot')
    
    # Redraw the canvas
    canvas.draw()

# Create a button to trigger the plot update
update_button = ttk.Button(root, text="Update Plot", command=update_plot)
update_button.pack()

# Run the Tkinter main loop
root.mainloop()
