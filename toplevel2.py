import tkinter as tk  # PEP8: `import *` is not preferred

# --- functions ---

def close_top():

    single_top.destroy()

    b['state'] = 'normal'
    
def open_top():
    global single_top

    b['state'] = 'disable'
    
    single_top = tk.Toplevel(root)
    l = tk.Label(single_top, text='TopLevel')
    l.pack()    
    single_top.protocol("WM_DELETE_WINDOW", close_top)
    
# --- main ---

root = tk.Tk()

b = tk.Button(root, text='TOP', command=open_top)
b.pack()

root.mainloop()