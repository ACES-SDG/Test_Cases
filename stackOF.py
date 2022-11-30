import tkinter as tk
from tkinter import ttk
import math

 

# Padding values.
tab_padx = (10, 0)
tab_pady = (20, 0)

# Font settings.
font_1 = ("Arial", 13, "bold")

# Main class.
class Main_GUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("DEMO")

        self.frame_blue_circle = BlueCircle(self, self)
        self.frame_green_square = GreenSquare(self, self)


        # Available shapes.
        self.available_shapes = ["CIRCLE", "SQUARE"]
        # Available colors.
        self.available_colors = ["BLUE", "GREEN"]

        # Function to run when color is changed.
        def color_change(*args):
            self.color = self.option_var_color.get()
            if self.color == "BLUE" and self.shape == "CIRCLE":
                self.type = "BlueCircle"
                self.show_frame("BlueCircle")
            elif self.color == "GREEN" and self.shape == "SQUARE":
                self.show_frame("GreenSquare")
            else:
                self.show_frame("Unimplemented")
            print(f"{self.color} {self.shape}")

        # Function to run when shape is changed.
        def shape_change(*args):
            self.shape = self.option_var_shape.get()
            if self.color == "BLUE" and self.shape == "CIRCLE":
                self.show_frame("BlueCircle")
            elif self.color == "GREEN" and self.shape == "SQUARE":
                self.show_frame("GreenSquare")
            else:
                self.show_frame("Unimplemented")
            print(f"{self.color} {self.shape}")


        #GUI tabs
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=1, column=0, sticky="w", padx=10, pady=10)

        #GUI tab1 - Type selection.
        self.tab1 = tk.Frame(self.nb)
        self.nb.add(self.tab1, text="Type")

        #GUI tab2 - Unput for selected type.
        self.tab2 = tk.Frame(self.nb)
        self.nb.add(self.tab2, text="Input")

        #GUI tab3 - Calculate result for selected type with its specific inputs.
        self.tab3 = tk.Frame(self.nb)
        self.nb.add(self.tab3, text="Result")

        # Tab-1 types.
        # Shapes.
        self.Label_shape = tk.Label(self.tab1, text = "Shape: ", font=font_1)
        self.Label_shape.grid(row=10, column=0, padx=tab_padx, pady=tab_pady, sticky="W")

        # Setup variable for disk type dropdown menu.
        self.option_var_shape= tk.StringVar()
        self.option_var_shape.set(self.available_shapes[0])
        self.option_var_shape.trace("w", shape_change)
        self.shape = self.option_var_shape.get()

        self.shape_dropdown_menu = tk.OptionMenu(self.tab1, self.option_var_shape, *self.available_shapes)
        self.shape_dropdown_menu.grid(row=10, column=1, sticky="WE", padx=tab_padx, pady=tab_pady)
        self.shape_dropdown_menu.config(font=font_1, width=20)
        self.shape_dropdown_menu["menu"].config(font=font_1)


        # Colors.
        self.Label_color = tk.Label(self.tab1, text = "Color: ", font=font_1)
        self.Label_color.grid(row=20, column=0, padx=tab_padx, pady=tab_pady, sticky="W")

        # Setup variable for disk type dropdown menu.
        self.option_var_color= tk.StringVar()
        self.option_var_color.set(self.available_colors[0])
        self.option_var_color.trace("w", color_change)
        self.color = self.option_var_color.get()

        self.color_dropdown_menu = tk.OptionMenu(self.tab1, self.option_var_color, *self.available_colors)
        self.color_dropdown_menu.grid(row=20, column=1, sticky="WE", padx=tab_padx, pady=tab_pady)
        self.color_dropdown_menu.config(font=font_1, width=20)
        self.color_dropdown_menu["menu"].config(font=font_1)


        # Tab-2. Show frame based on selection in Tab-1.
        # Container for frames.
        container = tk.Frame(self.tab2)
        container.grid(row=0, column=0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (BlueCircle, GreenSquare, Unimplemented):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("BlueCircle")


        # Tab-3. Calculate and display result based on Tab-1 and Tab-2.
        # Label to display result.
        result_text = "Result will be displayed here."
        self.Label_result = tk.Label(self.tab3, text = result_text, font=font_1, fg="RED")
        self.Label_result.grid(row=10, column=0, padx=tab_padx, pady=tab_pady, sticky="W")

        self.button = tk.Button(self.tab3, text=f"Print", command=self.print_info)
        self.button.grid(row=20, column=0, sticky="W")

        # print(self.Label_result)



    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def print_info(self):
        bc_text = f"Blue circle radius: {self.frame_blue_circle.radius}"
        print(bc_text)



# Class defining GUI for BlueCircle.
class BlueCircle(tk.Frame):

    def __init__(self, parent, controller, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.parent = parent
        self.radius = 0

        # Function to run when rim radius is changed.
        def Entry_change(*args):
            value = self.Entry_var_radius.get()
            
            if value == "":
                self.Entry_var_radius.set(".0")
            else:
                try:
                    self.radius = float(value)
                    print(self.radius)
                except ValueError:
                    self.Entry_var_radius.set("")
                    print(f"Warning! Floating point number only!")


        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Blue Circle", font=font_1, fg="BLUE")
        self.label.grid(row=0, column=0)
        self.label = tk.Label(self, text="Radius:")
        self.label.grid(row=1, column=0)

        # Setup variable for entry to use in callback trace.
        self.Entry_var_radius = tk.StringVar()
        self.Entry_var_radius.trace("w", lambda name, index, mode, sv=self.Entry_var_radius: Entry_change(self.Entry_var_radius))
        # Entry.
        self.Entry_radius = tk.Entry(self, font=font_1, textvariable=self.Entry_var_radius)
        self.Entry_radius.grid(row=1, column=1)
        self.radius = self.Entry_radius.get()


 
# Class defining GUI for GreenSquare.
class GreenSquare(tk.Frame):

    def __init__(self, parent, controller):

        super().__init__()
        self.parent = parent

        # Function to run when rim radius is changed.
        def Entry_change(*args):
            value = self.Entry_var_lenght.get()
            if value == "":
                self.Entry_var_lenght.set(".0")
            else:
                try:
                    self.lenght = float(value)
                    self.green_square_area = self.lenght**2
                    # print(f"Side lenght: {self.lenght}. Area: {self.green_square_area:.2f}")
                except ValueError:
                    self.Entry_var_lenght.set("")
                    print(f"Warning! Floating point number only!")


        # Inıtialize variable.
        self.green_square_area = 0


        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="Green Squire", font=font_1, fg="GREEN")
        self.label.grid(row=0, column=0)
        self.label = tk.Label(self, text="Side lenght:")
        self.label.grid(row=1, column=0)

        # Setup variable for entry to use in callback trace.
        self.Entry_var_lenght = tk.StringVar()
        self.Entry_var_lenght.trace("w", lambda name, index, mode, sv=self.Entry_var_lenght: Entry_change(self.Entry_var_lenght))
        # Entry.
        self.lenght = tk.Entry(self, font=font_1, textvariable=self.Entry_var_lenght)
        self.lenght.grid(row=1, column=1)
        self.lenght = self.Entry_var_lenght.get()


# Class defining GUI for unimplemented options.
class Unimplemented(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.label = tk.Label(self, text="To be implemented...", font=font_1, fg="RED")
        self.label.grid(row=0, column=0)



if __name__ == "__main__":
    app = Main_GUI()
    app.mainloop()