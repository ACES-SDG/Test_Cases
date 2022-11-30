from tkinter import *

root = Tk()    

users = ['Anne', 'Bea', 'Chris']

variables=[]

for x in range(len(users)):


    var_ejecutar=f"global {users[x]}"
    exec(var_ejecutar)

    var_ejecutar=f"{users[x]}=DoubleVar()"
    exec(var_ejecutar)

    variables.append(f"{users[x]}")

    var_ejecutar=f"""l = Checkbutton(root, text=\"{str(users[x])}\", 
        variable={str(users[x])},onvalue = "{str(users[x])}",offvalue = 0)"""
    exec(var_ejecutar)
    
    var_ejecutar="l.pack(anchor = 'w')"
    exec(var_ejecutar)


def get_val():

    for i in variables:

        var_ejecutar=f"print('baigan',{str(i)}.get())"
        exec(var_ejecutar)
        # print(i.get())
    print(variables)
btn= Button(root, text="ACTUALIZAR", state=NORMAL, command=get_val,bg="#C2CDD1") #crear boton
btn.pack(anchor = 'w')

root.mainloop()
