from tkinter import *

root = Tk()
root.geometry("500x400")
root.resizable(0,0)

h1 = Label(root,text = "Contact Us",fg="blue",font=('arial', 30,"bold"),bd=15).pack(side= TOP)
h1 = Label(root,text = "Name:",fg="black",font=('arial', 20,"bold"),bd=15).place(x=130,y=130,anchor=CENTER)
h2 = Label(root,text = "Ayush",fg="goldenrod",font=('arial', 20,"bold"),bd=15).place(x=240,y=130,anchor=CENTER)
h2 = Label(root,text = "Mobile No:",fg="black",font=('arial', 20,"bold"),bd=15).place(x=130,y=190,anchor=CENTER)
h3 = Label(root,text = "4568424742",fg="goldenrod",font=('arial', 20,"bold"),bd=15).place(x=290,y=190,anchor=CENTER)
h3 = Label(root,text = "Email:",fg="black",font=('arial', 20,"bold"),bd=15).place(x=70,y=250,anchor=CENTER)
h4 = Label(root,text = "starcdeveloper@gmail.com",fg="goldenrod",font=('arial', 20,"bold"),bd=15).place(x=310,y=250,anchor=CENTER)

root.mainloop()