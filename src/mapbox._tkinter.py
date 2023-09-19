import tkinter as tk
import webview

def open_map():
    webview.create_window('Map', 'https://www.mapbox.com/', width=800, height=600)

root = tk.Tk()
root.title('Mapbox Integration')

open_map_button = tk.Button(root, text='Open Map', command=open_map)
open_map_button.pack()

root.mainloop()
