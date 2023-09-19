import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import plotly.express as px
import dash
from dash import dcc, html
import threading
import tkinterhtml

DRAGGED_ITEM = None
drag_window = None

app = dash.Dash(__name__)

def run_dash():
    app.run_server(debug=False)

def open_browser():
    webbrowser.open('http://127.0.0.1:8050/')

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
    if not DRAGGED_ITEM:
        return
    x, y = event.widget.winfo_pointerxy()
    for drop_target in [row_area, column_area]:
        target_x, target_y, target_width, target_height = drop_target.winfo_rootx(), drop_target.winfo_rooty(), drop_target.winfo_width(), drop_target.winfo_height()
        if target_x < x < target_x + target_width and target_y < y < target_y + target_height:
            drop_target.config(text=DRAGGED_ITEM)
    event.widget.config(bg="lightblue", fg="black")
    event.widget.unbind("<B1-Motion>")
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
        widget.destroy()
    for header in df.columns:
        lbl = tk.Label(headers_frame, text=header, bg="lightblue")
        lbl.pack(padx=10, pady=5, fill=tk.X, expand=True)
        lbl.drag_data = {"type": "header", "value": header}
        lbl.bind("<Button-1>", on_drag_start)
        lbl.bind("<ButtonRelease-1>", on_drag_release)

def plot_chart():
    if chart_option.get() == "Barchart" and df is not None:
        row, col = row_area["text"], column_area["text"]
        if row and col and row in df.columns and col in df.columns:
            plt.figure(figsize=(10, 6))
            sns.barplot(x=df[row], y=df[col])
            canvas = FigureCanvasTkAgg(plt.gcf(), master=chart_frame)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            canvas.draw()
    elif chart_option.get() == "Scattermap" and df is not None:
        row, col = row_area["text"], column_area["text"]
        if row and col and row in df.columns and col in df.columns:
            valid_data = df.dropna(subset=[row, col])
            fig = px.scatter_geo(valid_data, lat=row, lon=col, projection="natural earth")
            app.layout = html.Div([dcc.Graph(figure=fig)])
            t1 = threading.Thread(target=run_dash)
            t1.start()
            # Embed browser in chart_frame
            html_frame = tkinterhtml.HtmlFrame(chart_frame)
            html_frame.set_content("<iframe src='http://127.0.0.1:8050/' width='800' height='600'></iframe>")

            html_frame.pack(fill=tk.BOTH, expand=True)

root = tk.Tk()
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
row_area.bind("<ButtonRelease-1>", on_drag_release)
column_area.bind("<ButtonRelease-1>", on_drag_release)
chart_option = ttk.Combobox(control_frame, values=["Barchart", "Scattermap"])
chart_option.pack(pady=20)
chart_option.set("Barchart")
chart_frame = tk.Frame(root)
chart_frame.pack(pady=20, fill=tk.BOTH, expand=True)
df = None
root.mainloop()
