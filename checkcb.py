import tkinter as tk

def done():
    result = []
    for var in variables:
        result.append(var.get())
   

root = tk.Tk()
names=['Modul 0', 'Modul 1', 'Modul 2', 'Modul 3', 'Modul 4', 'Modul 5', 'Modul 6', 'Modul 7', 'Modul 8', 'Modul 9']
variables = []
check_buttons = []
for i in names:
    var = tk.IntVar(root)
    check_button = tk.Checkbutton(root, text=i, variable=var)
    check_button.pack()
    

    variables.append(var)
    check_buttons.append(check_button)
    


done_button = tk.Button(root, text="Done", command=done)
done_button.pack()

root.mainloop()