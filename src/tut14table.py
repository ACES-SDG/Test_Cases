import tkinter as tk
from tkinter import filedialog, ttk, messagebox, Menu
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import webbrowser
import folium

root = tk.Tk()  # Create the main root window first

DRAGGED_ITEM = None  # global variable to hold the currently dragged item
drag_window = None  # To hold reference to the Toplevel window
df = None
SELECTED_COLUMNS = []  # This will hold the selected columns
agg_function = tk.StringVar(value="mean")  # Default aggregation function (Now initialized after the root window)

def reset_app():
    """Reset the application to its initial state."""
    global df, SELECTED_COLUMNS
    df = None
    SELECTED_COLUMNS = []

    # Clear column area labels
    row_area.config(text="Row")
    column_area.config(text="Column")

    # Clear headers frame
    for widget in headers_frame.winfo_children():
        widget.destroy()

    # Clear chart frame
    for widget in chart_frame.winfo_children():
        widget.destroy()
        
def display_table():
    """Display the dataframe as a table using ttk.Treeview."""
    for widget in chart_frame.winfo_children():
        widget.destroy()

    if df is None:
        return

    tree = ttk.Treeview(chart_frame, yscrollcommand=lambda f, l: vsb.set(f, l), xscrollcommand=lambda f, l: hsb.set(f, l))
    tree["columns"] = list(df.columns)
    tree["show"] = "headings"  # Hide the default column
    for col in df.columns:
        tree.column(col, width=100, anchor=tk.W)
        tree.heading(col, text=col, command=lambda c=col: on_header_click(tree, c))

    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.bind("<Button-3>", lambda event: on_header_right_click(event, tree))

    vsb = ttk.Scrollbar(chart_frame, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(chart_frame, orient="horizontal", command=tree.xview)

    tree.grid(row=0, column=0, sticky='nsew')
    vsb.grid(row=0, column=1, sticky='ns')
    hsb.grid(row=1, column=0, sticky='ew')

    chart_frame.grid_columnconfigure(0, weight=1)
    chart_frame.grid_rowconfigure(0, weight=1)

def on_header_click(tree, col):
    """Handle the click event on the treeview headers."""
    if col in SELECTED_COLUMNS:
        SELECTED_COLUMNS.remove(col)
        tree.heading(col, text=col)  # Reset the heading to its original state
    else:
        SELECTED_COLUMNS.append(col)
        tree.heading(col, text=f"[{col}]")  # Add brackets to show it's selected
  # Add brackets to show it's selected

def on_header_right_click(event, tree):
    """Handle right-click on treeview column headers."""
    col = tree.identify_column(event.x).split("#")[-1]
    if not SELECTED_COLUMNS:
        SELECTED_COLUMNS.append(col)
        tree.heading(col, text=f"[{col}]")  # Add brackets to show it's selected
    context_menu = Menu(root, tearoff=0)
    context_menu.add_command(label=f"Pivot by Selected Columns", command=pivot_table)
    context_menu.post(event.x_root, event.y_root)

def pivot_table():
    global df, SELECTED_COLUMNS
    try:
        if len(SELECTED_COLUMNS) < 2:
            raise ValueError("Please select at least one identifier column and one or more columns to pivot.")
        
        identifier_col = SELECTED_COLUMNS[0]  # The column dragged into row_area
        value_cols = SELECTED_COLUMNS[1:]  # All other columns dragged into column_area
        
        # Drop rows with NaN values in the selected columns
        valid_df = df.dropna(subset=[identifier_col] + value_cols)
        
        # Use the melt function to pivot the table
        # Set value_name to "PivotValue" to ensure uniqueness
        pivot_df = valid_df.melt(id_vars=identifier_col, value_vars=value_cols, 
                                 var_name='Question', value_name='PivotValue')
        
        df = pivot_df
        display_table()
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to pivot table. Reason: {str(e)}")
# This is the updated version of the pivot_table function.
# You should replace the original function in your code with this one.


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
    
    # Drop the columns that start with 'Unnamed'
    df = df.loc[:, ~df.columns.str.startswith('Unnamed')]

    for widget in headers_frame.winfo_children():
        widget.destroy()  # Clear any previous headers

    for header in df.columns:
        lbl = tk.Label(headers_frame, text=header, bg="lightblue")
        lbl.pack(padx=10, pady=5, fill=tk.X, expand=True)  # Changed from side=tk.LEFT to vertical packing
        lbl.drag_data = {"type": "header", "value": header}
        lbl.bind("<Button-1>", on_drag_start)
        lbl.bind("<ButtonRelease-1>", on_drag_release)


def plot_chart():
    option = chart_option.get()
    if option == "Barchart" and df is not None:
        row, col = row_area["text"], column_area["text"]
        if row and col and row in df.columns and col in df.columns:
            plt.figure(figsize=(10, 6))
            
            # Check which column is categorical to set orientation
            if df[row].dtype == 'O':
                sns.barplot(x=df[row], y=df[col])
            else:
                sns.barplot(y=df[row], x=df[col])

            for widget in chart_frame.winfo_children():
                widget.destroy()

            canvas = FigureCanvasTkAgg(plt.gcf(), master=chart_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas.draw()

    elif option == "Scattermap" and df is not None:
        lat_col, lon_col = row_area["text"], column_area["text"]
        if lat_col and lon_col and lat_col in df.columns and lon_col in df.columns:
            valid_rows = df.dropna(subset=[lat_col, lon_col])

            map_center = [valid_rows[lat_col].mean(), valid_rows[lon_col].mean()]
            m = folium.Map(location=map_center, zoom_start=10)

            for lat, lon in zip(valid_rows[lat_col], valid_rows[lon_col]):
                folium.Marker([lat, lon]).add_to(m)

            map_filename = "temp_map.html"
            m.save(map_filename)
            webbrowser.open(map_filename, new=2)
    elif option == "Table":
        display_table()




open_btn = tk.Button(root, text="Open File", command=on_open_file)
open_btn.pack(pady=20, padx=20)

headers_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
headers_frame.pack(pady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

control_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
control_frame.pack(pady=20, fill=tk.X, side=tk.TOP, expand=True)

row_area = tk.Label(control_frame, text="Row", bg="yellow", width=20, height=2)
row_area.pack(pady=10, side=tk.LEFT, padx=5, expand=True)

column_area = tk.Label(control_frame, text="Column", bg="yellow", width=20, height=2)
column_area.pack(pady=10, side=tk.LEFT, padx=5, expand=True)

reset_btn = tk.Button(root, text="Refresh", command=reset_app)
reset_btn.pack(pady=20, padx=20)


row_area.bind("<ButtonRelease-1>", on_drag_release)
column_area.bind("<ButtonRelease-1>", on_drag_release)

# Add the aggregation function dropdown inside the control_frame
agg_combobox = ttk.Combobox(control_frame, textvariable=agg_function)
agg_combobox['values'] = ["sum", "mean", "none"]
agg_combobox.pack(pady=20)
agg_combobox.set("mean")

chart_option = ttk.Combobox(control_frame)
chart_option['values'] = ["Barchart", "Scattermap", "Table"]
chart_option.pack(pady=20)
chart_option.set("Barchart")

chart_frame = tk.Frame(root)
chart_frame.pack(pady=20, fill=tk.BOTH, expand=True)

root.mainloop()