
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


class CollegeApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.container = ttk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        for F in (IndividPage ,counterPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(IndividPage)
        self.lift()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class IndividPage(ttk.Frame):

    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.userEntry()

    def userEntry(self):
        headingTest = Label(self, text="Enter your UserName:", font="Arial 20")
        headingTest.grid(row=0, column=0, pady=5, padx=5)

        self.usernameEnter = Entry(self, width=40)
        self.usernameEnter.grid(row=0, column=1, padx=5, pady=5)

        confirmBtn = Button(self, text="Confirm User", font="Arial 16",
                            command=self.confirm)

        confirmBtn.config(height=4, width=12)
        confirmBtn.grid(row=2, column=2, sticky=E, padx=45, pady=360)

    def confirm(self):
        if self.add_to_indivList():
            pass

    def add_to_indivList(self):
        global Individuals
        user = self.usernameEnter.get()
        if len(user) == 0:
            messagebox.showwarning(title='No user', message='Please enter a username!')
            return
        if self.usernameEnter.get():
            self.controller.show_frame(counterPage)

        if user in Individuals:
            messagebox.showwarning(title='In team', message=f'{user} is already in Individuals list!')

        Individuals.append(user)
        processedInd = list(dict.fromkeys(Individuals))
        self.controller.show_frame(counterPage)
        print(processedInd)
        print(len(Individuals))


class counterPage(ttk.Frame):
    def __init__(self, parent, controller):
        self.controller = controller
        ttk.Frame.__init__(self, parent)
        self.userEntry()

    def userEntry(self):

        self.usersInd = StringVar(self)
        self.usersInd.set(Individuals)
        indivSet = OptionMenu(self, self.usersInd, *Individuals)
        indivSet.grid(row=0, column=1, padx=10, pady=10)

        self.usersInd = StringVar(self)
        self.usersInd.set(Individuals)
        indivSet = OptionMenu(self, self.usersInd, *Individuals)
        indivSet.grid(row=0, column=0, padx=10, pady=10)

        backBtn = Button(self, text="BACK", font="Arial 16", height=2, width=6,
                         command=lambda: self.controller.show_frame(IndividPage))
        backBtn.grid(row=1, column=0, sticky=W, pady=245, padx=10)


if __name__ == '__main__':
    Individuals = []
    app = CollegeApp()
    app.geometry("800x500")
    app.resizable(False, False)
    app.title('Points Counter')
    app.mainloop()