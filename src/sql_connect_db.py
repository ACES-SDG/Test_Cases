import tkinter as tk
import mysql.connector
from tkinter import *
import pandas as pd
from list_class import MyListBox


def submitact():
	
	user = Username.get()
	passw = password.get()
	# Ip = ipaddress.get()

	print(f"The name entered by you is {user} {passw}")

	logintodb(user, passw)

def cols_call():
    sel_db = db_name_list.get(tk.ACTIVE)
    print(f'you selected "{sel_db}"')
    
    
	# colquery = 'select COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = "user_details" AND TABLE_NAME = "user_details"'  
	
	# try:
	# 	cursor.execute(colquery)
	# 	myresult = cursor.fetchall()
		
	# 	# Printing the result of the
	# 	# query
	# 	# print(myresult)

	# 	for i,x in enumerate(myresult):
	# 		T.insert(i, x)
			
	# 	print("Query Executed successfully")
	
	# except:
	# 	db.rollback()
	# 	print("Error occurred")


def logintodb(user, passw):
	
	# If password is entered by the
	# user
	if passw:
		db = mysql.connector.connect(host ='47.91.124.29',
									user = 'msweb_prd_mazhar',
									password = 'P)O(n@7830',
									db ="user_details")
		print("Connected to database successfully")
		# print(db ,'db')

		cursor = db.cursor()
		
		
	# If no password is entered by the
	# user
	else:
		db = mysql.connector.connect(host ="localhost",
									user = user,
									db ="College")
		cursor = db.cursor()
		
	# A Table in the database
	# savequery = "select * from user_details.user_details"
	# db_query = "SELECT TABLE_NAME FROM information_schema.tables WHERE table_schema = 'user_details';"
	try:
		# cursor.execute(db_query)
		sql_query = pd.read_sql_query(" SELECT * FROM user_details.user_details ", db)
		# print('cursor', cursor)
		print(sql_query.head())
		# dbs = cursor.fetchall()
		# print(dbs)
		# for db_name in dbs:
		# 	print(db_name[0].decode('utf-8'))
   			
		db_name_list.add_items(item_list=sql_query.columns)

			# db_name_list.insert(index, db_name)
			# lbl_db = tk.Label(db_name_frame, text =db_name[0].decode('utf-8'), )
			# lbl_db.pack(side='top')
			
			# db_btn = tk.Button(db_name_frame, text =db_name[0].decode('utf-8'),
			# 		fg='black',bg ='white') 
     				
			# db_btn.pack(side='top', )
			# lbl_db.bind('<Button-1>',lambda e: cols_call(lbl_db.cget('text')))
	except:
		# dbs.rollback()
		print("Error occurred")

def select_col_menu(event):
        try:
            listbox_menu.tk_popup(event.x_root, event.y_root)
        finally:
            listbox_menu.grab_release()
 	
root = tk.Tk()
root.geometry("1300x700")
root.title("DBMS Login Page")

# Defining the first row
lblIProw = tk.Label(root, text ="Ip-address -", )
lblIProw.place(x = 50, y = 90)

ipaddress = tk.Entry(root, width = 35)
ipaddress.place(x = 150, y = 90, width = 100)

# Defining the first row
lblfrstrow = tk.Label(root, text ="Username -", )
lblfrstrow.place(x = 50, y = 20)

Username = tk.Entry(root, width = 35)
Username.place(x = 150, y = 20, width = 100)

lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 50, y = 50)

password = tk.Entry(root, width = 35,show='*')
password.place(x = 150, y = 50, width = 100)

submitbtn = tk.Button(root, text ="Login",
					bg ='blue', command = submitact)
submitbtn.place(x = 150, y = 135, width = 55)

# T = Text(root, height = 5, width = 52)
cols = tk.Label(root, text ="Columns in your selected table")
cols.place(x = 550, y = 35)
T = Listbox(root, height = 15,
                  width = 30,)
T.place(x = 550, y = 55)

db_name_list = MyListBox(root,  width=40, height=20, justify=LEFT,
                                   borderwidth=0, relief=tk.FLAT, cursor='hand2', selectbackground="#5D6D7E")
db_name_list.place(x =350,y=50)

db_name_list.bind('<Button-3>', select_col_menu)

listbox_menu = Menu(db_name_list, tearoff=0)
listbox_menu.add_command(label="show cols of this tables", command=cols_call)
listbox_menu.add_command(label="dummy", command=None)


root.mainloop()
