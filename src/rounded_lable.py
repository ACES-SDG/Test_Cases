import customtkinter
import tkinter

def printing():
    print("================================sadnkjv afvjl")
root_tk = tkinter.Tk()

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# label = customtkinter.CTkLabel(master=root_tk, text="CTkLabel")
# label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# text_var = tkinter.StringVar(value="CTkLabel")

# label = customtkinter.CTkLabel(master=root_tk,
#                                textvariable=text_var,
#                                width=120,
#                                height=25,
#                                fg_color=("red", "gray75"),
#                                corner_radius=20)
# label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# label.bind(sequence='<Button-1>',func=lambda : printing())
# .bind( '<Button-1>',printing)

# button_ = customtkinter.CTkButton(master=root_tk,
#                             #    textvariable=text_var,
#                                width=120,
#                                height=25,command=printing,
#                                fg_color=("red", "gray75"),
#                                corner_radius=20)
# button_.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

# def combobox_callback(choice):
#     print("combobox dropdown clicked:", choice)

combobox_var = customtkinter.StringVar(value="option 2")
combobox = customtkinter.CTkComboBox(root_tk, values=["option 1", "option 2"],
                                     command=printing, variable=combobox_var,
                                     corner_radius=15)
combobox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
combobox_var.set("option 2")
root_tk.mainloop()