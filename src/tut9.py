import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import customtkinter as ctk
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


DRAGGED_ITEM = None  # global variable to hold the currently dragged item

drag_window = None  # To hold reference to the Toplevel window

def on_drag_start(event):
    global DRAGGED_ITEM, drag_window
    widget = event.widget
    widget.config(bg="darkblue", fg="white")  # Change background and foreground color
    DRAGGED_ITEM = widget.drag_data['value']
    
    # Create a Toplevel window that follows the cursor
    drag_window = tk.Toplevel(root)
    drag_window.overrideredirect(1)  # This removes window decorations
    label = tk.Label(drag_window, text=DRAGGED_ITEM, bg="lightblue")
    label.pack()
    drag_window.geometry(f"+{event.x_root}+{event.y_root}")  # Set position at the cursor
    
    # Update the Toplevel position while dragging
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_motion(event):
    """Update the Toplevel window position as you drag the item."""
    widget = event.widget
    x, y = widget.winfo_pointerxy()
    drag_window.geometry(f"+{x}+{y}")

def on_drag_release(event): 
    global DRAGGED_ITEM
    if not DRAGGED_ITEM:
        return

    x, y = event.widget.winfo_pointerxy()
    for drop_target in [row_area, column_area]:
        target_x, target_y, target_width, target_height = drop_target.winfo_rootx(), drop_target.winfo_rooty(), drop_target.winfo_width(), drop_target.winfo_height()
        if target_x < x < target_x + target_width and target_y < y < target_y + target_height:
            drop_target.config(text=DRAGGED_ITEM)

    event.widget.config(bg="lightblue", fg="black")  # Restore original appearance
    event.widget.unbind("<B1-Motion>")  # Unbind the motion event
    
    # Destroy the Toplevel window after dragging
    drag_window.destroy()
    DRAGGED_ITEM = None
    plot_chart()


    
def on_open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if not file_path:
        return

    global df
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    for widget in headers_frame.winfo_children():
        widget.destroy()  # Clear any previous headers
        
    for header in df.columns:
        lbl = tk.Label(headers_frame, text=header, bg="lightblue")
        lbl.pack(padx=10, pady=5, fill=tk.X, expand=True)  # Changed from side=tk.LEFT to vertical packing
        lbl.drag_data = {"type": "header", "value": header}
        lbl.bind("<Button-1>", on_drag_start)
        lbl.bind("<ButtonRelease-1>", on_drag_release)

def plot_chart():
    if chart_option.get() == "Barchart" and df is not None:
        row, col = row_area["text"], column_area["text"]
        if row and col and row in df.columns and col in df.columns:
            plt.figure(figsize=(10, 6))
            sns.barplot(x=df[row], y=df[col])
            
            for widget in chart_frame.winfo_children():
                widget.destroy()
                
            canvas = FigureCanvasTkAgg(plt.gcf(), master=chart_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas.draw()

root = tk.Tk()

open_btn = tk.Button(root, text="Open File", command=on_open_file)
open_btn.pack(pady=20, padx=20)

headers_frame = ctk.CTkScrollableFrame(master=root, width=300, height=200, corner_radius=0, fg_color="transparent")
headers_frame.pack(pady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)  # Side is set to LEFT to place it on the left

# headers_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
# headers_frame.pack(pady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)  # Side is set to LEFT to place it on the left

control_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
control_frame.pack(pady=20, fill=tk.X, side=tk.TOP,expand=True)

row_area = tk.Label(control_frame, text="Row", bg="yellow", width=20, height=2)
row_area.pack(pady=10, side=tk.LEFT, padx=5,expand=True)

column_area = tk.Label(control_frame, text="Column", bg="yellow", width=20, height=2)
column_area.pack(pady=10, side=tk.LEFT, padx=5,expand=True)

row_area.bind("<ButtonRelease-1>", on_drag_release)
column_area.bind("<ButtonRelease-1>", on_drag_release)

chart_option = ttk.Combobox(control_frame, values=["Barchart"])
chart_option.pack(pady=20)
chart_option.set("Barchart")

chart_frame = tk.Frame(root)
chart_frame.pack(pady=20, fill=tk.BOTH, expand=True)

df = None

root.mainloop()
