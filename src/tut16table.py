import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import pandas as pd

root = tk.Tk()
root.title("Data Pivoting Tool")

# Global variables
df = None  # The loaded dataframe
DRAGGED_ITEM = None
drag_window = None

# Drag and Drop functions
def on_drag_start(event):
    global DRAGGED_ITEM, drag_window
    widget = event.widget
    widget.config(bg="darkblue", fg="white")
    DRAGGED_ITEM = widget.drag_data['value']

    drag_window = tk.Toplevel(root)
    drag_window.overrideredirect(1)
    label = tk.Label(drag_window, text=DRAGGED_ITEM, bg="lightblue")
    label.pack()
    drag_window.geometry(f"+{event.x_root}+{event.y_root}")
    widget.bind("<B1-Motion>", on_drag_motion)

def on_drag_motion(event):
    widget = event.widget
    x, y = widget.winfo_pointerxy()
    drag_window.geometry(f"+{x}+{y}")

def on_drag_release(event):
    global DRAGGED_ITEM
    event.widget.config(bg="lightblue", fg="black")
    drag_window.destroy()
    DRAGGED_ITEM = None

def on_open_file():
    global df
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if not file_path:
        return

    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_excel(file_path)

    update_column_selectors(df.columns)

def update_column_selectors(columns):
    # Update column selectors
    index_dropdown['values'] = columns
    for col in columns:
        shown_columns_listbox.insert(tk.END, col)
        aggregated_columns_listbox.insert(tk.END, col)

def pivot_data():
    index_col = index_dropdown.get()
    shown_cols = [shown_columns_listbox.get(i) for i in shown_columns_listbox.curselection()]
    aggregated_cols = [aggregated_columns_listbox.get(i) for i in aggregated_columns_listbox.curselection()]

    if not index_col or not shown_cols or not aggregated_cols:
        messagebox.showwarning("Incomplete selection", "Please select all required columns for pivoting.")
        return

    melted_df = df.melt(id_vars=[index_col] + shown_cols, value_vars=aggregated_cols,
                        var_name='Aggregated column of question', value_name='Values')
    display_table(melted_df)

def display_table(data_df):
    for widget in chart_frame.winfo_children():
        widget.destroy()

    if data_df is None or data_df.empty:
        return

    tree = ttk.Treeview(chart_frame)
    tree["columns"] = list(data_df.columns)
    tree["show"] = "headings"
    for col in data_df.columns:
        tree.column(col, width=100, anchor=tk.W)
        tree.heading(col, text=col)

    for _, row in data_df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack(fill=tk.BOTH, expand=True)

# GUI design
open_btn = tk.Button(root, text="Open File", command=on_open_file)
open_btn.pack(pady=20, padx=20)

headers_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
headers_frame.pack(pady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

control_frame = tk.Frame(root, bg="white", bd=2, relief=tk.GROOVE)
control_frame.pack(pady=20, fill=tk.X, side=tk.TOP,expand=True)

# Dropdown for selecting index column
index_label = tk.Label(control_frame, text="Select Index Column:")
index_label.pack(pady=10, side=tk.LEFT, padx=5)
index_dropdown = ttk.Combobox(control_frame)
index_dropdown.pack(pady=10, side=tk.LEFT, padx=5)

# Listbox for selecting shown columns
shown_columns_label = tk.Label(control_frame, text="Columns to Show:")
shown_columns_label.pack(pady=10, side=tk.LEFT, padx=5)
shown_columns_listbox = tk.Listbox(control_frame, selectmode=tk.MULTIPLE, exportselection=False)
shown_columns_listbox.pack(pady=10, side=tk.LEFT, padx=5)

# Listbox for selecting aggregated columns
aggregated_columns_label = tk.Label(control_frame, text="Columns to Aggregate:")
aggregated_columns_label.pack(pady=10, side=tk.LEFT, padx=5)
aggregated_columns_listbox = tk.Listbox(control_frame, selectmode=tk.MULTIPLE, exportselection=False)
aggregated_columns_listbox.pack(pady=10, side=tk.LEFT, padx=5)

pivot_button = tk.Button(control_frame, text="Pivot Data", command=pivot_data)
pivot_button.pack(pady=20, side=tk.LEFT, padx=5)

chart_frame = tk.Frame(root)
chart_frame.pack(pady=20, fill=tk.BOTH, expand=True)

root.mainloop()
