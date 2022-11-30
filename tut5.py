from tkinter import *
from PIL import Image, ImageTk
root = Tk()
root.geometry("1255x944")

#photo = PhotoImage(file="1.png")
image = Image.open("photo.jpg")
photo = ImageTk.PhotoImage(image)
mazhar_image = Label(image=photo)
mazhar_image.pack()

root.mainloop()