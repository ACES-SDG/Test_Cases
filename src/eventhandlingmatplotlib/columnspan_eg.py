import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(root, text="Label 2")
label2.grid(row=1, column=0)

label3 = tk.Label(root, text="Label 3", bg='red')
label3.grid(row=0, column=1, columnspan=2)  # This label spans two columns

label4 = tk.Label(root, text="Label 4",bg='green')
label4.grid(row=1, column=1)

root.mainloop()
