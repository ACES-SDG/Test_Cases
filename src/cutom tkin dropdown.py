def find( obj ):
    name = f"{type(obj).__name__}:\n    "
    try:
        return name + "\n    ".join( [ f"{x} = '{obj.cget(x)}'" for x in obj.keys() if x not in ['bg', 'fg', 'bd']] )
    except:
        return f"'{obj}' has no keys attribute"


import tkinter as tk
from tkinter import filedialog as fido

root = tk.Tk()

root.geometry('500x500')

selection = tk.StringVar()

def show():
    label["text"] = selection.get()

label = tk.Label(root,text = selection.get())
label.pack()

drop = tk.OptionMenu(root,selection,'one','two','three')
drop.pack(pady = 10)


# Extra controls


image = fido.askopenfilename(title = "Choose a Picture")

if image:
    photo = tk.PhotoImage(file = image)
    photo_wide = photo.width()
    photo_high = photo.height()
    drop.config(height = photo_high, width = photo_wide,
                takefocus = 1, image = photo, compound = "center")
else:
    drop["height"] = '2'
    drop['width'] = '10'

drop["direction"] = ["above", "below", "flush", "left", "right"][2]
drop["anchor"] = ["n", "ne", "e", "se", "s", "sw", "w", "nw", "center"][0]
drop["justify"] = ["left", "right", "center"][1]
# drop["bitmap"] = "warning"
drop["background" ] = "cyan"
drop["activebackground" ] = "cyan"
drop["highlightbackground"] = "red"
drop["font"] = 'TkDefaultFont 14'

drop["menu"]["background"] = "red"
drop["menu"]["foreground"] = "yellow"
drop["menu"]["font"] = "TkDefaultFont 15"
drop["menu"]["selectcolor"] = "green"
drop["menu"]["activeborderwidth"] = '4'

button = tk.Button(root, text = 'show', command = show)
button.pack(pady = 10)

print(find( drop ))
print(find( drop[ "menu" ] ))

root.mainloop()