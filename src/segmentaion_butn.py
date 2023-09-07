import customtkinter
import tkinter
def segmented_button_callback(value):
    print("segmented button clicked:", value)


app = tkinter.Tk()
segemented_button_var = customtkinter.StringVar(value="Value 1")
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback,
                                                     variable=segemented_button_var)
segemented_button.pack()
app.mainloop()