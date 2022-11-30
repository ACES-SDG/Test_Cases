import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import tix
from turtle import left, width

from matplotlib.pyplot import text
from pyparsing import originalTextFor
from filemenu import createMenu
from Treeview import *
from SheetsPage import menuiconframe
from DataSource import*


LARGEFONT =("Arial", 35)

class OceanApp(tix.Tk):
	
	# __init__ function for class tkinterApp
	def __init__(self, *args, **kwargs):
		
		# __init__ function fo-+r class Tk
		tix.Tk.__init__(self, *args, **kwargs)
		
		screen_width = self.winfo_screenwidth()
		screen_height = self.winfo_screenheight()
		# creating a container
		container = tix.Frame(self)
		container.pack(side = "top", fill = "both", expand = True)

		container.grid_rowconfigure(0, weight = 1)
		container.grid_columnconfigure(0, weight = 1)

		# initializing frames to an empty array
		self.frames = {}
		createMenu(self)
		
		global file_path,navigation_frame
		file_path = Label(self, bg="#e7e7e6", width=screen_width ,relief=GROOVE, anchor="w")  # diplaying the file path which is being imported
		file_path.pack_propagate(0)
		file_path.pack(side=BOTTOM)
		# file_path[text

		font_details = ('Arial', 11)
		navigation_frame = Frame(self, borderwidth=3, relief=GROOVE, width=screen_width, height=30)
		navigation_frame.pack_propagate(0)
		# tip = tix.Balloon(self)

		navigation_frame.pack(side=BOTTOM,fill=X)
		
		# iterating through a tuple consisting
		# of the different page layouts
		for F in (Data_Source, Sheets, DashBoard):
			CWF = F
			print(screen_height)
			frame = F(container, self)

			# initializing frame of that object from
			# Data Source, Sheets, DashBoard respectively with
			# for loop
			self.frames[F] = frame

			frame.grid(row = 0, column = 0, sticky ="nsew")	
		self.show_frame(Data_Source)

	# to display the current frame passed as
	# parameter
	
	def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

# first CWF frame Data Source

class Data_Source(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		

		screen_width = self.winfo_screenwidth()
		# showNavigationFrame(self,screen_width)
		sideframe_datasource(self)
		Treeview_display(self)

		data_source_btn = Button(navigation_frame, fg="black", text="Data Source", relief=GROOVE
		,command=lambda : DataSource.Datasource)
		# data_source_btn.configure(font=font_details)
		data_source_btn.pack(side=LEFT, padx=1)

		Sheet_btn = Button(navigation_frame, fg="black", text="Sheet", relief=GROOVE
		,command=lambda : controller.show_frame(Sheets))
		# data_source_btn.configure(font=font_details)
		Sheet_btn.pack(side=LEFT, padx=1)

		Dashboard_btn = Button(navigation_frame, fg="black", text="Dashboard", relief=GROOVE
		,command=lambda : controller.show_frame(DashBoard))
		# data_source_btn.configure(font=font_details)
		Dashboard_btn.pack(side=LEFT, padx=1)

		# label of frame Layout 2
		# label = ttk.Label(self, text ="Data Source", font = LARGEFONT)
		#
		# # putting the grid in its place by using
		# # grid
		# label.pack(side='top')*9*9+-
		screen_width = self.winfo_screenwidth()
		


# second CWF frame Sheets
class Sheets(tk.Frame):
	
	def __init__(self, parent, controller):
		
		tk.Frame.__init__(self, parent)
		

		screen_width = self.winfo_screenwidth()
		# showNavigationFrame(self,screen_width)
		menuiconframe(self)
		sidePanel(self)
		row_col_frame(self,screen_width)
		plots(self)

# third CWF frame DashBoard
class DashBoard(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		
		menuiconframe(self)
		
		screen_width = self.winfo_screenwidth()
		# showNavigationFrame(self,screen_width)
		label = ttk.Label(self, text ="Dashboard", font = LARGEFONT)
		label.pack(side=TOP, padx = 10, pady = 10)

		

# Driver Code
app = OceanApp()
app.geometry('1300x750')
app.title('Ocean Desktop Beta')
app.minsize(1200, 650)
app.iconbitmap("Logo.ico")
app.mainloop()
