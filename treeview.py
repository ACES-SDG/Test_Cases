from tkinter import *
import tkinter
import tkinter.ttk as ttk
import csv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import plotly.express as px
from sklearn.linear_model import LinearRegression


data = pd.read_csv("2019-2020.csv")
x = np.array(data[["gender","distance","scholarship","stanine"]])
y = np.array(data["enrolled_2021"])

xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.24,random_state=40)

model = LinearRegression()
model.fit(xtrain,ytrain)

features = np.array(data[["gender","distance","scholarship","stanine"]])


root = tkinter.Tk()
root.title("FAITH Enrollment Prediction Simulator")
root.geometry("900x500")

TableMargin = Frame(root, width=300)
TableMargin.pack(side=RIGHT)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, 
columns=("student_no", "gender", "distance", "scholarship", "stanine", "prediction"), height=400, 
selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('student_no', text="Student No.", anchor=W)
tree.heading('gender', text="Gender", anchor=W)
tree.heading('distance', text="Distance in KM", anchor=W)
tree.heading('scholarship', text="Scholarship", anchor=W)
tree.heading('stanine', text="STANINE Rank", anchor=W)
tree.heading('prediction', text="Prediction in %", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=100)
tree.column('#2', stretch=NO, minwidth=0, width=100)
tree.column('#3', stretch=NO, minwidth=0, width=100)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=100)
tree.pack()

with open('2019-2020.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
for row in reader:
    student_no = row['student_no']
    gender = row['gender']
    distance = row['distance']
    scholarship = row['scholarship']
    stanine = row['stanine']
    tree.insert("", 0, values=(student_no, gender, distance, scholarship, stanine))

def predict():
    pred = model.predict(features) * 100
    for x in pred:
        tree.insert("", 'end', values=('','','','','', x))


b1 = Button(root, text='Predict', command=predict, height = 2, width = 20, bg='#081947', fg='#fff',)
b1.pack(padx=15, pady=200)
#============================INITIALIZATION==============================
if __name__ == '__main__':
    root.mainloop()